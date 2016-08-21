from ..common.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(128))
    token = db.Column(db.String(128))
