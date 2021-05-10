from models import Category


def categories():
    return Category.query.order_by(Category.name.asc()).all()
