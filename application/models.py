#!/usr/bin/python3

from application import db

class Questions(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    question = db.Column(db.String(100),
                         nullable=False)
    answers = db.relationship('Answers',
                              backref='question')

class Employees(db.Model):
    name = db.Column(db.String(30), primary_key=True)
    answers = db.relationship('Answers',
                              backref='employee')

class Answers(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    answer = db.Column(db.String(7))
    question_id = db.Column('questions_id',
                            db.Integer,
                            db.ForeignKey('questions.id'))
    employee_id = db.Column('employees_name',
                            db.String(30),
                            db.ForeignKey('employees.name'))
