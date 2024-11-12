FROM python:3.12.1-slim

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && apt-get clean

# Копирование файла с зависимостями
COPY requirements.txt /app/
WORKDIR /app

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование основного приложения
COPY app.py /app/

# Команда для запуска приложения
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
