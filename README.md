# Это web приложение где пользователь вводит название города и получает прогноз погоды и количество осадков на неделю.


Фреймворк использован `Django` и `django-rest-framework`
- АPI для погоды использован https://open-meteo.com/
- API для автодополнения использован https://nominatim.openstreetmap.org
- Для реализации API использован `django-rest-framework`
- Сохраняется история поиска для каждого пользователя, и есть API, показывающее сколько раз вводили какой город
- Реализованы графики для удобного просмотра данных
- Всё это помещено в докер контейнер
- Написаны тесты


## Подготовка
Сначала подгатавливаем директорию и виртуальное окружение для проекта:
```bash
mkdir p ~/dev/tests/; cd ~/dev/tests/
python -m venv test_ocomplex
cd test_ocomplex
. bin/activate
mkdir src; cd src
```
Клонируем проект `git clone https://github.com/vitaldmit/weather.git .`


## Далее есть два способа запуска проекта:
❶ Запуск в контейнерах `Docker`:
```bash
cp env.example .env
sed -i 's/DEBUG = True/DEBUG = False/g' .env
docker-compose up --build
```
После проверки можно запустить `docker-compose down -v`

❷ Запуск в стандартном виртуальном окржении:
```bash
pip install -U pip
pip install -r requirements.txt
cp env.example .env
sed -i 's/DEBUG = False/DEBUG = True/g' .env
python manage.py makemigrations; python manage.py makemigrations weather; python manage.py migrate
python manage.py test
python manage.py test
```

## Cкриншот
![Screenshot 2024-07-21 10 15 33](https://github.com/user-attachments/assets/5f80c511-5ba0-4296-894e-9ce7f0035fb9)
