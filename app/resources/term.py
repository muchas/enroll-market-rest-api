from flask import jsonify
from flask.views import MethodView
from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from webargs.flaskparser import use_args
from ..models import Term, DayEnum, Offer


class StudentSchema(Schema):
    id = fields.Integer()
    name = fields.String(attribute="full_name")


class TeacherSchema(Schema):
    id = fields.Integer()
    name = fields.String(attribute="full_name")


class RoomSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    floor = fields.Integer()


class SubjectSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class TimeSchema(Schema):
    day = EnumField(DayEnum, by_value=True)
    start = fields.Time()
    end = fields.Time()


class TermSchema(Schema):
    id = fields.Integer()
    room = fields.Nested(RoomSchema, only=["name", "floor"])
    subject = fields.Nested(SubjectSchema)
    teacher = fields.Nested(TeacherSchema)
    time = fields.Function(lambda obj: TimeSchema().dump(obj).data)


class OfferSchema(Schema):
    id = fields.Integer()
    term = fields.Nested(TermSchema)
    student = fields.Nested(StudentSchema)
    created = fields.DateTime()


class OfferCreationSchema(Schema):
    term_id = fields.Integer()
    student_id = fields.Integer()

    class Meta:
        strict = True


class OfferListView(MethodView):
    def get(self):
        offers = Offer.query.filter_by(is_available=True)
        return jsonify(OfferSchema().dump(offers, many=True).data)

    @use_args(OfferCreationSchema())
    def post(self, args):
        import pdb; pdb.set_trace()
        pass


class TermResource(MethodView):
    def get(self, term_id):
        term = Term.query.get(term_id)
        return jsonify(TermSchema().dump(term).data)


class TermListResource(MethodView):
    def get(self):
        terms = Term.query.all()
        return jsonify(TermSchema().dump(terms, many=True).data)


class MyTermListResource(MethodView):
    def get(self):
        terms = Term.query.all()
        return jsonify(TermSchema().dump(terms, many=True).data)
