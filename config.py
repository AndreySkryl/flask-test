class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin:qwerty@localhost/auto_shop?auth_plugin=mysql_native_password'
    SECRET_KEY = 'something very secret'

    # Flask-security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
