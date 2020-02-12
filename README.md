# О проекте
Проект представляет из себя web-SPA (Single Page Application), позволяющий искать количество определенных слов на той или иной странице в интернете. Frontend выполнен с помощью фреймворка Vue, Backend - с помощью фреймворка Django. 
Проект предполагает упаковку приложения в Docker-контейнер и публикацию контейнера на платформе Heroku. Деплой контейнера осуществляется с помощью файла `heroku.yml`
# Инструкция
  - [Склонировать](https://github.com/geterodyn/search_spa.git) проект в локальную директорию 
  - Создать приложение в Heroku:
    `heroku create your-app-name`
  - Установить тип стека приложения в зачение "контейер":
    `heroku stack:set container`
  - Установить плагины Redis и Postgresql для своего приложения:
    ```
    heroku addons:create heroku-redis:hobby-dev -a your-app-name
    heroku addons:create heroku-postgresql:hobby-dev -a your-app-name
    ```
    В результате появятся две переменные среды `DATABASE_URL` и `REDIS_URL`, которые мы используем в настройках нашего приложения
  - 
