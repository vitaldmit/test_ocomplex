# Используем официальный образ Python 3.12
FROM python:3.12

# Устанавливаем переменную окружения для работы Python в неинтерактивном режиме
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Запускаем миграции
RUN python manage.py migrate

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

RUN cp prod_settings.py weather_project/
