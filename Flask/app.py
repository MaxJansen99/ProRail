from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from routes import *
from models import *

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)