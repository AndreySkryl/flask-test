from flask import Blueprint, render_template
from models import SparePart

spare_parts = Blueprint('spare_parts', __name__, template_folder='templates')


@spare_parts.route('/')
def index():
    spare_parts = SparePart.query.all()

    return render_template('spare_parts/index.html', spare_parts=spare_parts)


# http://localhost/spare_parts/<slug>
@spare_parts.route('/<slug>')
def spare_part_detail(slug):
    spare_part = SparePart.query.filter(SparePart.slug == slug).first()
    return render_template('spare_parts/spare_part_detail.html', spare_part=spare_part)
