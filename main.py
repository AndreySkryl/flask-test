from app import app
from app import db

from spare_parts.blueprint import spare_parts

import view

app.register_blueprint(spare_parts, url_prefix='/spare_parts')

if __name__ == '__main__':
    app.run(debug=True)
