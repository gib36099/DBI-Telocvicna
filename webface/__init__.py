import flask
from flask_misaka import Misaka

app = flask.Flask(__name__)
Misaka(app)
app.secret_key = b'Ka78584554lorst Josef os.urandom(24)'

from . import routes
from . import models