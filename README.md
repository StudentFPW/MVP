## Установка:
1. Клонируйте репозиторий на свой компьютер
2. Установите и активируйте виртуальное виртуальное окружение в папке с проектом:
```
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```
cd skidkalov
pip install -r requirements.txt
```

4. Создайте и примените миграции

    **ВАЖНО**: сперва выполнить команду:

    `python3 manage.py makemigrations`

    только после этого:
   
    `python3 manage.py migrate`

5. Создайте суперпользователя:

   `python3 manage.py createsuperuser`

   Укажите email и пароль для суперюзера (username не запрашивается).
  
6. Запуск сервера:

    `python3 manage.py runserver`

## Настройка OAuth.

1. Перейдите в админ панель http://127.0.0.1:8000/admin/ и войдите под суперпользователем.

2. В разделе DJANGO OAUTH TOOLKIT - Applications создайте 3 приложения:

   - поля **Client id**, **Client secret**, не трогать;

     **ВАЖНО!!!** **Client secret** нужно скопировать себе до сохранения приложения, после создания приложения он будет захеширован.

     Если **Client secret** не был скопирован, нужно пересоздать приложение и скопировать его до сохранения приложения.
  
   - поля **Redirect uris** и **Post logout redirect uris** оставить пустыми;
  
   - в поле **User** выбрать ранее созданного суперюзера из списка;
  
   - **Client type** установить *Public*;
  
   - **Authorization grant** type установить *Resource owner password-based*;
  
   - **Name** (опционально) - Yandex, Google, VKontakte, в соответствии с OAuth провайдерами.

     Каждое созданное приложение будет регистрировать/аутентифицировать пользователей и выдавать токены доступа. Одно приложение может работать только с одним провайдером.
     
     **Client id** и **Client secret** должен знать фронэнд для направления запроса на сервер.

     
## Реализовано:
1. Описаны модели БД
2. Настроена регистрация пользователя с подтверждением по e-mail и авторизация по токену;
3. Прописаны энд-поинты для регистрации через VK, Google, Yandex.
4. 
## TODO
Подключить JWT-токены
