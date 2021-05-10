from flask import Flask
from flask import redirect, url_for, request

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)  # ORM (Object-Relational Mapping, рус. объектно-реляционное отображение, или преобразование)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ADMIN
from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class CategoryAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'spare_parts']


class SparePartAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'price', 'amount', 'description', 'category']


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView())
admin.add_view(CategoryAdminView(Category, db.session, name='Категории'))
admin.add_view(SparePartAdminView(SparePart, db.session, name='Запчасти'))

admin.add_view(AdminView(User, db.session, name='Пользователи'))
admin.add_view(AdminView(Role, db.session, name='Роли'))


# Flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
