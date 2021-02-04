#!/usr/bin/python3

from application import db

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)
