from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin


def slugify(s: str) -> str:
    modified_s = re.sub(r'[^\w+]', '-', s.lower())
    modified_s = re.sub(r'-+', '-', modified_s)

    dic = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
           'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
           'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
           'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'yi',
           'э': 'e', 'ю': 'yu', 'я': 'ya'}
    table = str.maketrans(dic)
    modified_s = modified_s.translate(table)

    if modified_s.startswith('-'):
        modified_s = modified_s[1:]
    if modified_s.endswith('-'):
        modified_s = modified_s[:-1]

    return modified_s


spare_parts__tags = db.Table(
    'spare_parts__tags',
    db.Column('spare_part_id', db.Integer, db.ForeignKey('spare_part.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class SparePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)  # ЧПУ (URL)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(SparePart, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=spare_parts__tags, backref=db.backref('spare_parts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'SparePart<id: {self.id}, title: {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return self.name


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


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
