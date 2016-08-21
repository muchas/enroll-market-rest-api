import enum
from sqlalchemy_utils import ChoiceType

from ..common.database import db


student_terms = db.Table('student_terms',
        db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
        db.Column('term_id', db.Integer, db.ForeignKey('term.id'))
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    terms = db.relationship('Term', secondary=student_terms,
                            backref=db.backref('students', lazy='dynamic'))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Student>'


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Teacher>'


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Subject>'


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    floor = db.Column(db.Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Room>'


class Day(enum.Enum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6


class Term(db.Model):
    """

    """
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    day = db.Column(ChoiceType(Day, impl=db.Integer()))
    start = db.Column(db.Time)
    end = db.Column(db.Time)

    teacher = db.relationship('Teacher', backref=db.backref('terms', lazy='dynamic'))
    room = db.relationship('Room', backref=db.backref('terms', lazy='dynamic'))
    subject = db.relationship('Subject', backref=db.backref('terms', lazy='dynamic'))

    def __init__(self):
        pass

    def __repr__(self):
        return '<Term %r>' % self.username
