# -*- encoding: utf-8 -*-
from app.models import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.Datetime, nullable=False)
    update_date = db.Column(db.Datetime, nullable=False)
