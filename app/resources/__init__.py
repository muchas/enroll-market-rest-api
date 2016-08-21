from flask import Blueprint
from flask_restful import Api

from .term import Term, TermList, MyTermList

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


api.add_resource(Term, '/terms/<term_id>')
api.add_resource(TermList, '/terms')
api.add_resource(MyTermList, '/me/terms')
