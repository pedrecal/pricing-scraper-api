from flask import Flask

from configs.db import initialize_db
from configs.google_auth import initialize_auth
from flask_restful import Api
from middleware.error_handling_middleware import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

from routes import initialize_routes

api = Api(app, errors=errors)

initialize_db(app)
oauth = initialize_auth(app)
initialize_routes(api, args={'oauth': oauth})