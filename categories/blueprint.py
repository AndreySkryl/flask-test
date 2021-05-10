from flask import Blueprint, request
from flask import render_template

from models import Category, SparePart
from menu import categories

category_bp = Blueprint('category_bp', __name__, template_folder='templates')


@category_bp.route('/<slug>')
def category_detail(slug):
    # q = request.args.get('q')
    # if q:
    #     spare_parts = SparePart.query.filter(SparePart.title.contains(q) | SparePart.description.contains(q))
    # else:
    #     spare_parts = SparePart.query.order_by(SparePart.created.desc())

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    category = Category.query.filter(Category.slug == slug).first_or_404()
    spare_parts = SparePart.query.filter(SparePart.category_id == category.id)
    spare_parts_as_pages = spare_parts.paginate(page=page, per_page=4)

    return render_template('categories/category_detail.html', categories=categories(), category=category,
                           spare_parts_as_pages=spare_parts_as_pages)
