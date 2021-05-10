from app import app

from categories.blueprint import category_bp
from spare_parts.blueprint import spare_part_bp


app.register_blueprint(category_bp, url_prefix='/categories')
app.register_blueprint(spare_part_bp, url_prefix='/spare_parts')
