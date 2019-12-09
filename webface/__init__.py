import flask

app = flask.Flask(__name__)
app.secret_key = b'Ka78584554lorst Josef os.urandom(24)'

from . import routes
