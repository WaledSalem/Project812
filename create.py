#!/usr/bin/python3

from application import db

db.session.remove()
db.drop_all()
db.create_all()
