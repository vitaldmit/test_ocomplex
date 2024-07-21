# Тестовое задание от компании O-COMPLEX

## Это web приложение где пользователь вводит название города и получает прогноз погоды в этом городе на ближайшее время.

❗ Выполнены все пункты задания.

Фреймворк использован `Django` и `django-rest-framework`.
- АPI для погоды использован https://open-meteo.com/
- API для автодополнения использован https://nominatim.openstreetmap.org
- Для реализации API использован `django-rest-framework`
- Также реализованы графики для удобного просмотра температуры и осадков.

## Установка и запуск.
Сначала подгатавливаем директорию и виртуальное окружение для проекта:
```bash
mkdir p ~/dev/tests/; cd ~/dev/tests/
python -m venv test_ocomplex
cd test_ocomplex
. bin/activate
mkdir src; cd src
```
Клонируем проект `git clone https://github.com/vitaldmit/test_ocomplex.git .`

**Далее есть два способа запуска проекта:**

1. Запуск в контейнерах `Docker`:
```bash
cp env.example .env
docker-compose up --build
```
После проверки можно запустить `docker-compose down -v`

2. Запуск в стандартном виртуальное окржение:
- Обновляем `PIP` командой `pip install --upgrade pip`
- Устанавливаем зависимости `pip install -r requirements.txt`
- Создаем файл `.env` на основе `env.example` с помощью команды `cp env.example .env`
- Выполняем миграции `python manage.py makemigrations; python manage.py makemigrations weather; python manage.py migrate`
- Запускаем сервер `python manage.py runserver`
- Для запуска тестов команда `python manage.py test`


#### Демонстрация сайта доступна по ссылке http://vitaldmit.fvds.ru
#### Демонстрация API доступна по ссылке http://vitaldmit.fvds.ru/api/city-search-count/

Проект по ссылке запущен на `Docker` контейнерах.

![Screenshot 2024-07-21 10 15 33](https://github.com/user-attachments/assets/5f80c511-5ba0-4296-894e-9ce7f0035fb9)

