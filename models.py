from datetime import datetime

from app import db
from model_utils import slugify

from flask_security import UserMixin, RoleMixin


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(255), unique=True)  # ЧПУ (URL)
    spare_parts = db.relationship('SparePart', backref='category', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return self.name


class SparePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(255), unique=True)  # ЧПУ (URL)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, *args, **kwargs):
        super(SparePart, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return self.title


# Flask Security
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'User<email: {self.email}>'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'Role<name: {self.name}>'
