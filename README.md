##TaskTracker

Приложение для учета задач

####API

Приложение предоставляет API для:
* создания проекта
* CRUD задач в проекте с неколькими описаниями
* просмотра комментариев, добавления комментариев к задачам
* просмотра информации по задаче
* просмотра комментариев к каждой задаче

####Запуск приложения

`python manage.py migrate` - создать базу данных с нужными таблицами
`python manage.py createsuperuser` - создать супер-юзера - админа
`python manage.py runserver` - запустить сервис локально

В Docker:

Создать файл-конфигурацию:

    FROM python:3
    WORKDIR /task_tracker
    ADD requirements.txt /task_tracker/
    RUN pip install -r requirements.txt
    ADD . /task_tracker/

И файл `docker-compose.yml`, в котором будут указаны все параметры разворачивания: база данных, накатка миграций, запуск сервиса и прочее
