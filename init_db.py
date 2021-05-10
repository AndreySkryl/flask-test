import json
import os

from app import db
from app import user_datastore
from models import User, Role, Category, SparePart

# создаём пользователя и даём ему роль администратора
user_datastore.create_user(email='admin@admin.ru', password='admin')
db.session.commit()

user_datastore.create_role(name='admin', description='administrator')
db.session.commit()

user = User.query.first()
role = Role.query.first()
user_datastore.add_role_to_user(user, role)
db.session.commit()


# создаём категории и наполняем их данными из JSON-файлов
category_names = ['Масла и автохимия', 'Шины и диски', 'Автоэлектроника']
categories = [Category(name=name) for name in category_names]
for category in categories:
    db.session.add(category)
db.session.commit()

filename = 'spare_parts.json'
for category_name in category_names:
    full_filename = os.path.join('.', 'data', 'categories', category_name, filename)
    if os.path.isfile(full_filename):
        with open(full_filename, 'rt', encoding='utf-8') as json_file:
            category = Category.query.filter(Category.name == category_name).first()

            json_spare_parts = json.load(json_file)
            spare_parts = [
                SparePart(
                    title=json_spare_part['title'],
                    price=json_spare_part['price'],
                    amount=json_spare_part['amount'],
                    description=json_spare_part['description'],

                    category_id=category.id
                ) for json_spare_part in json_spare_parts
            ]
            db.session.add_all(spare_parts)
            db.session.commit()
