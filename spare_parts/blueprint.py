from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from app import db
from models import SparePart, Tag

from .forms import SparePartForm


spare_parts = Blueprint('spare_parts', __name__, template_folder='templates')


@spare_parts.route('/create', methods=['POST', 'GET'])
def create_spare_part():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        amount = request.form['amount']
        description = request.form['description']

        try:
            spare_part = SparePart(title=title, price=price, amount=amount, description=description)
            db.session.add(spare_part)
            db.session.commit()
        except Exception as ex:
            print('Error: insert row (spare_part) in DB')
            print(ex)

        return redirect(url_for('spare_parts.index'))

    form = SparePartForm()
    return render_template('spare_parts/create_spare_part.html', form=form)


@spare_parts.route('/')
def index():
    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        spare_parts = SparePart.query.filter(SparePart.title.contains(q) | SparePart.description.contains(q))
    else:
        spare_parts = SparePart.query.order_by(SparePart.created.desc())

    pages = spare_parts.paginate(page=page, per_page=5)

    return render_template('spare_parts/index.html', spare_parts=spare_parts, pages=pages)


# http://localhost/spare_parts/<slug>
@spare_parts.route('/<slug>')
def spare_part_detail(slug):
    spare_part = SparePart.query.filter(SparePart.slug == slug).first()
    tags = spare_part.tags
    return render_template('spare_parts/spare_part_detail.html', spare_part=spare_part, tags=tags)


@spare_parts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    _spare_parts = tag.spare_parts.all()
    return render_template('spare_parts/tag_detail.html', tag=tag, spare_parts=_spare_parts)
