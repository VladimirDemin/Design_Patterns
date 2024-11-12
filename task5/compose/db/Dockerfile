FROM postgres:16.2-alpine

# Установка необходимых утилит
RUN apk add --no-cache curl tar

# Копирование архива Liquibase в контейнер
COPY liquibase-4.29.2.tar.gz /tmp/

# Распаковка Liquibase и перемещение в /usr/local/bin
RUN tar -xzf /tmp/liquibase-4.29.2.tar.gz -C /tmp/ \
    && mv /tmp/liquibase /usr/local/bin/ \
    && rm /tmp/liquibase-4.29.2.tar.gz

# Копирование миграций
COPY migrations/ /docker-entrypoint-initdb.d/

CMD ["postgres"]
