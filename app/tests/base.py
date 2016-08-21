from flask_testing import TestCase

from app import app
from app.common.database import db


class ResourceTestCase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        self.session = db.session
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

