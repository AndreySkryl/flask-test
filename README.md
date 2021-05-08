# flask-test

Для создания таблиц в БД необходимо выполнить:
```cmd
python manage.py db upgrade
```
После чего просто запускаем проект:
```cmd
python main.py
```


# База данных (команды)

Для создания папки с миграциями
```cmd
python manage.py db init
```

Для создания миграции
```cmd
python manage.py db migrate
```

Для накатывания миграции
```cmd
python manage.py db upgrade
```

Для откатывания миграции
```cmd
python manage.py db downgrade
```