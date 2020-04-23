from __future__ import annotations

import datetime
from typing import Dict

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db, login_manager

DATE_FMT = "%Y-%m-%dT%H:%M:%S"


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(length=30), nullable=True)
    last_name = db.Column(db.String(length=50), nullable=True)
    email = db.Column(db.String(length=100), unique=True, index=True)
    is_web_admin = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return f"User<{self.id}>"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def password(self):
        raise AttributeError("'password' is not a readable attribute.")

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str):
        return check_password_hash(self.password_hash, password)

    def to_json(self) -> Dict:
        json_user = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "last_seen": self.last_seen.strftime(DATE_FMT),
            "is_web_admin": self.is_webadmin
        }
        return json_user

    def ping(self):
        self.last_seen = datetime.datetime.utcnow()
        db.session.add(self)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.filter_by(id=int(user_id)).first()
