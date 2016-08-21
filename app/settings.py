import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://smucha:password@localhost/enroll_market'
DATABASE_CONNECT_OPTIONS = {}

SECRET_KEY = "secret"

URL_PREFIX = '/api'

PRESERVE_CONTEXT_ON_EXCEPTION = False
