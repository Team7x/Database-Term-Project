from flask import Flask
from flask.ext.scss import Scss

app = Flask(__name__)

app.debug = True
Scss(app, static_dir='static', asset_dir='Database-Term-Project\items\static\assets\scss')

from items import main