from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from app import db, login_manager

bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(32), unique=True, nullable=False)
  lastname = db.Column(db.String(32), unique=True, nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(64), nullable=False)

  def set_password(self, password):
    self.password = bcrypt.generate_password_hash(password).decode("utf-8")

  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)