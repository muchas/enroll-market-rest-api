from flask import Blueprint

from .term import TermResource, TermListResource, MyTermListResource, OfferListView

api_blueprint = Blueprint('api', __name__)

api_blueprint.add_url_rule('/terms/<int:term_id>', view_func=TermResource.as_view('terms-detail'))
api_blueprint.add_url_rule('/terms', view_func=TermListResource.as_view('terms'))
api_blueprint.add_url_rule('/me/terms', view_func=MyTermListResource.as_view('terms-me'))
api_blueprint.add_url_rule('/offers', view_func=OfferListView.as_view('offers'))
