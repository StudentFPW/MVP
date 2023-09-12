## Установка:
1. Клонируйте репозиторий на свой компьютер
2. Установите и активируйте виртуальное виртуальное окружение в папке с проектом:
```
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```
cd backend
pip install -r requirements.txt
```

4. Создайте и примените миграции

    **ВАЖНО**: сперва выполнить команду:

    `python3 manage.py makemigrations`

    только после этого:
   
    `python3 manage.py migrate`

5. Создайте суперпользователя:

   `python3 manage.py createsuperuser`

   Укажите email, firstname, lastname и пароль для суперюзера.
  
6. Запуск сервера:
    
    http:

    `python3 manage.py runserver`

    https:

    `python3 manage.py runsslserver`
     
7. Запуск celery worker:

    'celery -A config worker -l INFO -B'

## API Documentation.

    Swagger UI: `http://127.0.0.1:8000/swagger/` 
    Yaml: `http://127.0.0.1:8000/swagger.yaml/` 
    JSON: `http://127.0.0.1:8000/swagger.json/` 


## Настройка OAuth.

1. Перейдите в админ панель http://127.0.0.1:8000/admin/ и войдите под суперпользователем.

2. В разделе DJANGO OAUTH TOOLKIT - Applications создайте 3 приложения:

   - поля **Client id**, **Client secret**, не трогать;
     
     **Client id** и **Client secret** должен знать фронтэнд для направления запроса на сервер.

     **ВАЖНО!!!** **Client secret** нужно скопировать себе до сохранения приложения, после создания приложения он будет захеширован.

     Если **Client secret** не был скопирован, нужно пересоздать приложение и скопировать его до сохранения приложения.
  
   - поля **Redirect uris** и **Post logout redirect uris** оставить пустыми;
  
   - в поле **User** выбрать ранее созданного суперюзера из списка;
  
   - **Client type** установить *Confidential*;
  
   - **Authorization grant** type установить *Resource owner password-based*;
  
   - **Name** (опционально) - Yandex, Google, VKontakte, в соответствии с OAuth провайдерами.

     Каждое созданное приложение будет регистрировать/аутентифицировать пользователей и выдавать токены доступа. Одно приложение может работать только с одним провайдером.


## Реализовано:
1. Описаны модели БД;
2. Настроена регистрация пользователя с подтверждением по e-mail и авторизация по токену;
3. Прописаны энд-поинты для регистрации через VK, Google, Yandex;
4. Отправка уведомлений в личный кабинет и на почту об увеличении скидки, нахождении товара и окончании срока отслеживания;
5. 


## TODO
Подключить JWT-токены
