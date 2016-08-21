from flask_restful import Resource


class Term(Resource):
    def get(self, term_id):
        return {'hello': 'world'}

    def put(self, term_id):
        return {'hello': 'world'}


class TermList(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}


class MyTermList(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}
