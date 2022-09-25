# TODO_keep

---

### Задание

Разработать REST-сервис для создания заметок к проектам.</br>

- Для backend использовать `Django Rest Framework`</br>
- Для frontend использовать `React.js`</br>
- Авторизация должна происходит с помощью JWT token</br>
- Написать тесты для API</br>
- Завернуть всё в контейнер`Docker(Docker-compose)`

### ***Объект User***

- uid - идентификатор
- username - логин
- first_name - имя
- last_name - фамилия
- email - почта
- created - когда создан пользователь
- modified - когда изменен пользователь
- is_active - статус активности (True, False)
- is_staff - статус персонала (True, False)
- is_superuser - статус администратора (True, False)

### ***Объект Project***

- uid - идентификатор
- name - название проекта
- repository - ссылка на удаленный репозитории
- creators_project - создатели проекта

### ***Объект TODO***

- uid - идентификатор
- body - название проекта
- creator_keep - создатель заметки
- project - проект, к которому создана заметка
- created - когда создана заметка
- modified - когда изменена заметка
- is_active - статус заметки(Активна, Закрыта)

---

### ***API поддерживает операции***

1. Users
    - получить список User(GET)
    - получить User по его uid(GET)
    - обновить User(PUT, PATCH)
2. TODOS
    - создать TODO(POST)
    - получить список TODO(GET)
    - получить TODO по его uid(GET)
    - обновить TODO(PUT, PATCH)
    - удалить TODO(DELETE)
3. Projects
    - создать Projects(POST)
    - получить список Projects(GET)
    - получить Projects по его uid(GET)
    - обновить Projects(PUT, PATCH)
    - удалить Projects(DELETE)

Также можно ознакомиться с документацией пройдя по адресу `/redoc/`

---

## Установка и настройка

Клонировать проект

```
https://github.com/Arseny-Chistyakov/TODO.git
```

Создать виртуальное окружение

```
python -m venv venv
```

Активировать виртуальное окружение

```
venv\Scripts\activate.bat
```

Установить зависимости

```
pip install -r requirements.txt
```

Создать .env файл и заполнить

```
SECRET_KEY = 'your value'
#database
TEST_NAME = 'your value'
NAME = 'your value'
USER = 'your value'
PASSWORD = 'your value'
HOST = 'your value'
PORT = 'your value'
#createsuperuser in command "python manage.py create_users"
USERNAME_ADMIN = 'your value'
PASSWORD_ADMIN = 'your value'
```

Перейти в каталог приложения, создать миграции, применить их

```
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя

```
python manage.py createsuperuser
```

Запустить сервер

```
python manage.py runserver
```

---

## Тестирование API

Перейти в каталог приложения.<br>
Запустить тесты с помощью команды:

```
python manage.py test
...
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........................
----------------------------------------------------------------------
Ran 26 tests in 3.535s

OK
Destroying test database for alias 'default'...
```

## Запуск Docker

Перейти в каталог приложения.<br>
Запустить приложения с нуля: создать сети, если нужно, собрать Dockerfile и запустить контейнера.
Если добавить параметр `-d`, то приложение запуститься в фоновом процессе.

```
docker-compose -f docker-compose.yml up -d
...
Creating postgres_TODO ... done
Creating backend_TODO  ... done
Creating nginx_TODO    ... done
Creating frontend_TODO ... done

```

Проверить состояние контейнеров

```
docker-compose -f docker-compose.yml ps

    Name                   Command               State           Ports         
-------------------------------------------------------------------------------
backend_TODO    bash -c  python manage.py  ...   Up      0.0.0.0:8080->8080/tcp
frontend_TODO   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp
nginx_TODO      /docker-entrypoint.sh ngin ...   Up      0.0.0.0:8000->80/tcp
postgres_TODO   docker-entrypoint.sh postgres    Up      5432/tcp
```

Перейти по адресу для проверки [127.0.0.1:80](127.0.0.1:80)

---

## License

[MIT License](LICENSE.md) (c) arseny.v.chistyakov