from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('default_config')
db = SQLAlchemy(app,use_native_unicode='utf8')