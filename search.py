from flask import request

from models import SparePart


def get_page():
    page = request.args.get('page')
    page = int(page) if page and page.isdigit() else 1
    return page


def get_spare_parts_by_q():
    q = request.args.get('q')
    if q:
        spare_parts = SparePart.query.filter(SparePart.title.contains(q) | SparePart.description.contains(q))
    else:
        spare_parts = SparePart.query.order_by(SparePart.created.desc())

    return spare_parts
