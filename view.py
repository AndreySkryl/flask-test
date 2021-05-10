from flask import render_template

from app import app
from menu import categories
from search import get_page, get_spare_parts_by_q


@app.route('/')
def index():
    return render_template('index.html', categories=categories())


@app.route('/about')
def about():
    return render_template('about.html', categories=categories())


@app.route('/search')
def search():
    page = get_page()
    spare_parts = get_spare_parts_by_q()
    spare_parts_as_pages = spare_parts.paginate(page=page, per_page=4)
    return render_template('search.html', categories=categories(), spare_parts_as_pages=spare_parts_as_pages)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', categories=categories()), 404
