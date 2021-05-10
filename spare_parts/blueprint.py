from flask import Blueprint
from flask import render_template

from flask import request

from flask import redirect
from flask import url_for

from flask_security import login_required

from app import db

from models import Category, SparePart
from .forms import SparePartForm


spare_part_bp = Blueprint('spare_part_bp', __name__, template_folder='templates')


# @spare_part_bp.route('/create', methods=['POST', 'GET'])
# @login_required
# def create_spare_part():
#     if request.method == 'POST':
#         title = request.form['title']
#         price = request.form['price']
#         amount = request.form['amount']
#         description = request.form['description']
#
#         try:
#             spare_part = SparePart(title=title, price=price, amount=amount, description=description)
#             db.session.add(spare_part)
#             db.session.commit()
#         except Exception as ex:
#             print('Error: insert row (spare_part) in DB')
#             print(ex)
#
#         return redirect(url_for('spare_parts.index'))
#
#     form = SparePartForm()
#     return render_template('spare_parts/create_spare_part.html', form=form)
#
#
# @spare_part_bp.route('/<slug>/edit', methods=['POST', 'GET'])
# @login_required
# def edit_spare_part(slug):
#     spare_part = SparePart.query.filter(SparePart.slug == slug).first_or_404()
#
#     if request.method == 'POST':
#         form = SparePartForm(formdata=request.form, obj=spare_part)
#         form.populate_obj(spare_part)
#         db.session.commit()
#
#         return redirect(url_for('spare_parts.spare_part_detail', slug=spare_part.slug))
#
#     form = SparePartForm(obj=spare_part)
#     return render_template('spare_parts/edit_spare_part.html', spare_part=spare_part, form=form)


# @spare_part_bp.route('/')
# def index():
#
#
#     page = request.args.get('page')
#
#     if page and page.isdigit():
#         page = int(page)
#     else:
#         page = 1
#
#     # q = request.args.get('q')
#     # if q:
#     #     spare_parts = SparePart.query.filter(SparePart.title.contains(q) | SparePart.description.contains(q))
#     # else:
#     #     spare_parts = SparePart.query.order_by(SparePart.created.desc())
#
#     pages = spare_parts.paginate(page=page, per_page=5)
#
#     categories = Category.query.all()
#     return render_template('spare_parts/index.html', categories=categories, pages=pages)


# http://localhost/spare_parts/<slug>
@spare_part_bp.route('/<slug>')
def spare_part_detail(slug):
    spare_part = SparePart.query.filter(SparePart.slug == slug).first_or_404()

    categories = Category.query.all()
    return render_template('spare_parts/spare_part_detail.html', categories=categories,
                           spare_part=spare_part, category=spare_part.category)


# @spare_part_bp.route('/category/<slug>')
# def category_list(slug):
#     category = Category.query.filter(Category.slug == slug).first_or_404()
#     _spare_parts = category.spare_parts.all()
#     return render_template('spare_parts/category_detail.html', category=category, spare_parts=_spare_parts)
