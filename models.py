from app import db
from datetime import datetime
import re


def slugify(s: str) -> str:
    pattern = r'[^\w+]'
    modified_s = re.sub(pattern, '-', s.lower())
    return re.sub(r'-+', '-', modified_s)


spare_parts__tags = db.Table('spare_parts__tags',
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
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'<Tag id: {self.id}, name: {self.name}>'
