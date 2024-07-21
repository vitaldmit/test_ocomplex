# Тестовое задание от компании O-COMPLEX

## Это web приложение где пользователь вводит название города и получает прогноз погоды в этом городе на ближайшее время.

Выполнены все пункты задания, но упаковка в `Docker` контейнеры немного не доделана.

Фреймворк использован `Django` и `django-rest-framework`.
- АPI для погоды использован https://open-meteo.com/
- API для автодополнения использован https://nominatim.openstreetmap.org
- Для реализации API использован `django-rest-framework`
- Также реализованы графики для удобного просмотра температуры и осадков.

## Установка и запуск.
1. Так как `Docker` контейнеры еще не до конца реализованы, предлагаю создать и настроить виртуальное окружение 
```bash
mkdir p ~/dev/tetsts/; cd ~/dev/tests/
python -m venv test_ocomplex
cd test_ocomplex
. bin/activate
mkdir src; cd src
```
2. Необходимо склонировать проект `git clone https://github.com/vitaldmit/test_ocomplex.git .`
3. Обновляем `PIP` командой `pip install --upgrade pip`
4. Устанавливаем зависимости `pip install -r requirements.txt`
5. Создаем файл `.env` на основе `.env.example` с помощью команды `cp .env.example .env`
6. В файле `.env` необходимо указать `SECRET_KEY`
7. Выполняем миграции `python manage.py makemigrations; python manage.py makemigrations weather` и `python manage.py migrate`
8. Запускаем сервер `python manage.py runserver`
9. Для запуска тестов команда `python manage.py test`


#### Демонстрация сайта доступна по ссылке http://vitaldmit.fvds.ru:8000
#### Демонстрация API доступна по ссылке http://vitaldmit.fvds.ru:8000/api/city-search-count/

![Screenshot 2024-07-21 10 15 33](https://github.com/user-attachments/assets/5f80c511-5ba0-4296-894e-9ce7f0035fb9)

