rem задаём кодировку UTF-8
chcp 65001

rem создаём структуру БД
call init_db.cmd

rem инициализируем начальными данными БД
call python init_db.py