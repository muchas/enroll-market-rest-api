from flask import Flask
from flask_migrate import Migrate

from .common.database import db
from .resources import api_blueprint
from .models import *


app = Flask(__name__)
app.config.from_object('app.settings')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api_blueprint, url_prefix=app.config['URL_PREFIX'])
