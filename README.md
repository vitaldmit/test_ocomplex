# Тестовое задание от компании O-COMPLEX

## Это web приложение где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

Выполнены все пункты задания, но упаковка в `Docker` контейнеры немного не доделана.

Фреймворк использован `Django` и `django-rest-framework`.
- АPI для погоды использован https://open-meteo.com/
- API для автодополнения использован https://nominatim.openstreetmap.org
- Для реализации API использован `django-rest-framework`
- Также реализованы графиики для удобного просмотрания данных.

## Установка и запуск.
1. Т.к. `Docker` контейнеры еще не до конца реализованы, предлагаю создать и настроить виртуальное окружение 
```bash
mkdir ~/dev; cd ~/dev
python -m venv weather
cd weather
. bin/activate
mkdir src; cd src
```
2. Необходимо склонировать проект `git clone https://github.com/vitaldmit/test_ocomplex.git .`
3. Устанавливаем зависимости `pip install -r requirements.txt`
4. Создать файл `.env` на основе `.env.example` с помощью команды `cp .env.example .env`
5. В файле `.env` необходимо указать `SECRET_KEY`
6. Выполняем миграции `python manage.py makemigrations` и `python manage.py migrate`
7. Запускаем сервер `python manage.py runserver`
8. Для запуска тестов `python manage.py test`
9. Для проверки API используется ссылка `/api/city-search-count/`


#### Демонстрация сайта доступна по ссылке http://vitaldmit.fvds.ru:8000
#### Демонстрация API доступна по ссылке http://vitaldmit.fvds.ru:8000/api/city-search-count/

![2024-07-19_16-01](https://github.com/user-attachments/assets/ad684463-c505-478a-b061-a5ea40d6e5d9)
