import datetime
import factory
from factory.fuzzy import FuzzyInteger, FuzzyDateTime
from faker import Factory as FakerFactory
from pytz import UTC
from app.models import Term, Student, Teacher, Room, Subject, Offer
from app.common.database import db


faker = FakerFactory.create()


class StudentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Student
        sqlalchemy_session = db.session

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())


class TeacherFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Teacher
        sqlalchemy_session = db.session

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())


class RoomFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Room
        sqlalchemy_session = db.session

    name = factory.Sequence(lambda n: u'Room %d' % n)
    floor = FuzzyInteger(-1, 4)


class SubjectFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Subject
        sqlalchemy_session = db.session

    name = factory.Sequence(lambda n: u'Subject %d' % n)


class TermFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Term
        sqlalchemy_session = db.session

    teacher = factory.SubFactory(TeacherFactory)
    room = factory.SubFactory(RoomFactory)
    subject = factory.SubFactory(SubjectFactory)
    day = FuzzyInteger(0, 4)
    start = FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=UTC))
    end = FuzzyDateTime(datetime.datetime(2010, 1, 1, tzinfo=UTC))


class OfferFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Offer
        sqlalchemy_session = db.session
