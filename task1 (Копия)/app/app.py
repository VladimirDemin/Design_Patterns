import os

from typing import Iterable
from prometheus_client import generate_latest
from flask import Flask
from random import randint

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.metrics import Observation, CallbackOptions
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


app = Flask(__name__)


def rand_number():
    with tracer.start_as_current_span("do_roll"):
        res = randint(1, 100)
        current_span = trace.get_current_span()
        current_span.set_attribute("roll.value", res)
        return res


def do_important_job():
    with tracer.start_as_current_span("do_important_job"):
        randint(1, 10000)


@app.route("/number")
def random():
    request_counter.add(1)
    result = rand_number()
    do_important_job()
    if (result < 0 or result > 100):
        return 'something went wrong!', 500
    return str(result)


@app.route('/metrics')
def get_metrics():
    return generate_latest()


def cpu_time_callback(options: CallbackOptions) -> Iterable[Observation]:
    observations = []
    with open("/proc/stat") as procstat:
        procstat.readline()  # skip the first line
        for line in procstat:
            if not line.startswith("cpu"):
                break
            cpu, *states = line.split()
            observations.append(Observation(
                int(states[0]) // 100, {"cpu": cpu, "state": "user"}))
            observations.append(Observation(
                int(states[1]) // 100, {"cpu": cpu, "state": "system"}))
    return observations


def init_traces(resource):
    tracer_provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(
        endpoint=os.environ.get('TRACE_ENDPOINT', "http://localhost:4317")))
    tracer_provider.add_span_processor(processor)
    trace.set_tracer_provider(tracer_provider)
    tracer = trace.get_tracer(__name__)
    return tracer


def init_metrics(resource):
    metric_reader = PrometheusMetricReader()
    meter_provider = MeterProvider(
        resource=resource, metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider)

    meter = metrics.get_meter_provider().get_meter(__name__)
    request_counter = meter.create_counter(
        name="request_counter", description="Number of requests", unit="1")
    meter.create_observable_counter(
        "system.cpu.time",
        callbacks=[cpu_time_callback],
        unit="s",
        description="CPU time"
    )
    return request_counter


resource = Resource.create({SERVICE_NAME: os.environ.get(
    'APP_SERVICE_NAME', "my-python-service")})
tracer = init_traces(resource)
request_counter = init_metrics(resource)

FlaskInstrumentor().instrument_app(app)

if __name__ == "__main__":
    host = os.environ.get('APP_HOST_NAME', "0.0.0.0")
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host=host, port=port)

