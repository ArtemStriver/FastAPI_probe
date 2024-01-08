# FastAPI_probe
______________
**FastAPI_probe** - проект по изучению и освоению используемых технологий.

## Используемые технологии
______________

![version](https://img.shields.io/badge/python-3.12-blue)


![package](https://img.shields.io/badge/FastAPI-0.105.0-red)
![package](https://img.shields.io/badge/SQLAlchemy-2.0.23-red)
![package](https://img.shields.io/badge/alembic-1.13.0-red)
![package](https://img.shields.io/badge/aiohttp-3.9.1-red)
![package](https://img.shields.io/badge/WebSockets-12.0-red)
![package](https://img.shields.io/badge/Pytest-7.4.3-red)

![package](https://img.shields.io/badge/PostgreSQL-185)
![package](https://img.shields.io/badge/Redis-139)
![package](https://img.shields.io/badge/Celery-139)
![package](https://img.shields.io/badge/Flower-139)
![package](https://img.shields.io/badge/Docker-169)


![license](https://img.shields.io/badge/license-Apache__License__V2.0-green)

## Описание
______________

Проект выполнен как API для сайта с содержанием отчета по инвестициям, имеет простой графический 
интерфейс. Основная цель - отработка навыков работы с **Fast API** в связке 
с **SQLAlchemy** и **alembic**, в качестве базы данных использована **PostgreSQL**, 
**Redis** с **Celery** и **Flower** для кэширования и создания очереди задач,
есть модуль чата, сделанный на основе **WebSocket** соединения. В проекте присутствуют 
тесты для базовых эндпоинтов, с применением **pytest**. Проект контейнеризирован с 
помощью **dockerfile** и **docker-compose** - его можно запустить из контейнера.
 
#### ***Проект поддерживает следующий функционал:***
- Регистрация, аутентификация и авторизация пользователей;
- Работу с базой данных - создание, удаление, поиск данных;
- Отправку на email сообщений с отчетом;
- Общий чат на основе websocket;
- Графическое представление в виде простого html оформления.


## Установка и настройка
______________

***Локально:***

Скачиваем репозиторий со всеми файлами с GitHub.
Создаем виртуальное окружение, но можно в коренную папку, и загружаем туда все необходимые пакеты
с помощью команды: 
``` python
pip install -r requirements.txt
```
Создаем и заполняем файл .env своими данными:
``` bash
cat .env-example > .env
```
Создаем миграции и обновляем их:
``` python
alembic revision --autogenerate -m "migrations" 

alembic upgrade head
```
Запускаем проект локально:
``` python
uvicorn src.main:app --reload
```

***С помощью Docker:***

Для начала установите [docker](https://docs.docker.com/engine/install/) 
на свой компьютер, после перейдите в главную папку с проектом и
создайте и заполните файл .env своими данными:
``` bash
cat .env-example > .env
```
Затем в терминале введите команду:
``` docker
docker compose up
```

## Лицензия
______________

Проект разработан с использованием лицензии [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)