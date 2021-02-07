#!/usr/bin/python3
#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOME_KEY'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://waled:root@localhost/data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = False
db = SQLAlchemy(app)

from application import routes

