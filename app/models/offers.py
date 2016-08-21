from sqlalchemy_utils import Timestamp

from ..common.database import db


class Offer(db.Model, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    is_available = db.Column(db.Boolean, default=True)

    term = db.relationship('Term', backref=db.backref('offers', lazy='dynamic'))
    student = db.relationship('Student', backref=db.backref('offers', lazy='dynamic'))

    def __init__(self):
        pass

    def __repr__(self):
        return "<Offer>"
