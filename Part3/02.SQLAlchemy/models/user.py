from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)  # 추가된 필드
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')

	