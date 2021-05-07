from app import db
from datetime import datetime
import re


def slugify(s: str) -> str:
    pattern = r'[^\w+]'
    modified_s = re.sub(pattern, '-', s.lower())
    return re.sub(r'-+', '-', modified_s)


class SparePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True) # ЧПУ (URL)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(SparePart, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'SparePart<id: {self.id}, title: {self.title}>'
