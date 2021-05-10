set DB_NAME=auto_shop
set DB_ROOT_LOGIN=root
set DB_ROOT_PASSWORD=asdqwe123
rem создание БД
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "DROP DATABASE IF EXISTS %DB_NAME%;"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "CREATE DATABASE %DB_NAME%;"


set DB_ADMIN_LOGIN=admin
set DB_ADMIN_PASSWORD=qwerty
rem создание пользователя "администратор" для БД
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "DROP USER IF EXISTS '%DB_ADMIN_LOGIN%'@'localhost';"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "CREATE USER '%DB_ADMIN_LOGIN%'@'localhost' IDENTIFIED WITH mysql_native_password BY '%DB_ADMIN_PASSWORD%';"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "GRANT ALL PRIVILEGES ON %DB_NAME%.* TO '%DB_ADMIN_LOGIN%'@'localhost';"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "FLUSH PRIVILEGES;"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "UPDATE mysql.user SET plugin='mysql_native_password' WHERE host='localhost' AND user='%DB_ADMIN_LOGIN%';"
call mysql -u %DB_ROOT_LOGIN% -p%DB_ROOT_PASSWORD% -e "FLUSH PRIVILEGES;"

rem удаляем старые миграции
call rm -rf .\migrations

rem создаём таблицы БД с помощью ORM SQLAlchemy
call python manage.py db init
call python manage.py db migrate
call python manage.py db upgrade
