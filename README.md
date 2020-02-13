# О проекте
Проект представляет из себя web-SPA (Single Page Application), позволяющий искать количество определенных слов на той или иной странице в интернете. Frontend выполнен с помощью фреймворка Vue, Backend - с помощью фреймворка Django. Задача по поиску ставится на исполнение в очередь Celery, её параметры заносятся в базу данных Postgres, результат её выполнения сохраняется в хранилище Redis, после обновления результат также заносится в БД.
Проект предполагает упаковку приложения в Docker-контейнер и публикацию контейнера на платформе Heroku. Деплой контейнера осуществляется с помощью файла `heroku.yml`
# Инструкция
  - [Склонировать](https://github.com/geterodyn/search_spa.git) проект в локальную директорию
  ```
  git clone https://github.com/geterodyn/search_spa.git
  ```
  - Создать приложение в Heroku:
  ```
  heroku create your-app-name
  ```
  - Установить тип стека приложения в значение "контейнер":
  ```
  heroku stack:set container
  ```
  - Установить плагины Redis и Postgresql для своего приложения:
  ```
    heroku addons:create heroku-redis:hobby-dev -a your-app-name
    heroku addons:create heroku-postgresql:hobby-dev -a your-app-name
  ```
  В результате появятся две переменные среды на Хероку _`DATABASE_URL`_ и _`REDIS_URL`_, которые мы используем в настройках нашего приложения
  - Начать сборку контейнера и деплой на Хероку
  ```
  git push heroku master
  ```
  - Включить работу worker dyno:
  ```
  heroku ps:scale worker=1
  ```
  - Примените начальные миграции
  ```
  heroku run sh
  $ python3 manage.py makemigrations
  $ python3 manage.py migrate
  ```
  
В итоге, приложение будет доступно по адресу `https://your-app-name.herokuapp.com`
