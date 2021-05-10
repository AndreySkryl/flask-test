# Пример приложения на Flask (магазин автозапчастей)

## Инициализация

Для установки всех необходимых библиотек достаточно набрать:
```cmd
pip install -r requirements.txt
```

Перед запуском скрипта для инициализации БД `init.cmd` необходимо 
указать `логин` и `пароль` пользователя "`root`" базы данных 
в файле "`init_db.cmd`" (строки `2` и `3`):
```cmd
DB_ROOT_LOGIN=<логин пользователя root БД>
DB_ROOT_PASSWORD=<пароль пользователя root БД>
```

Для инициализации структуры БД и наполнения её исходными данными:
```cmd
init.cmd
```


## Запуск

Команда для запуска приложения:
```cmd
python main.py
```


## (*) База данных (команды)

Для создания папки с миграциями:
```cmd
python manage.py db init
```

Для создания миграции:
```cmd
python manage.py db migrate
```

Для накатывания миграции:
```cmd
python manage.py db upgrade
```

Для откатывания миграции:
```cmd
python manage.py db downgrade
```