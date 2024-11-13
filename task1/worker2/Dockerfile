# worker2/Dockerfile
# Используем Python как базовый образ
FROM python:3.8-slim

# Создаем рабочую директорию
WORKDIR /usr/src/app

# Копируем скрипт в контейнер
COPY script.py .

# Команда для запуска скрипта
CMD ["python", "./script.py"]
