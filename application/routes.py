#!/usr/bin/python3

from application import app, db
from application.models import Employees, Answers
from flask import render_template, request, redirect, url_for
from application.forms import BasicForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BasicForm()
    if form.validate_on_submit():
        new_employee = Employees(employee=form.name.data)
        new_employee_id = Answers(employee_id=Employees.id)
        new_answer1 = Answers(answer=form.answer1.data, question_id=1)
        new_answer2 = Answers(answer=form.answer2.data, question_id=2)
        new_answer3 = Answers(answer=form.answer3.data, question_id=3)
        new_answer4 = Answers(answer=form.answer4.data, question_id=4)
        new_answer5 = Answers(answer=form.answer5.data, question_id=5)
        new_answer6 = Answers(answer=form.answer6.data, question_id=6)
        new_answer7 = Answers(answer=form.answer7.data, question_id=7)
        new_answer8 = Answers(answer=form.answer8.data, question_id=8)
        new_answer9 = Answers(answer=form.answer9.data, question_id=9)
        new_answer10 = Answers(answer=form.answer10.data, question_id=10)
        new_answer11 = Answers(answer=form.answer11.data, question_id=11)
        new_answer12 = Answers(answer=form.answer12.data, question_id=12)
        new_answer13 = Answers(answer=form.answer13.data, question_id=13)
        db.session.add_all([new_employee, new_employee_id,
                            new_answer1, new_answer2, new_answer3, new_answer4,
                            new_answer5, new_answer6, new_answer7, new_answer8,
                            new_answer8, new_answer9, new_answer10,
                            new_answer11, new_answer12, new_answer13])
        db.session.commit()
        return render_template('home.html',
                               form=form,
                               employee=new_employee)
    else:
        return render_template('add.html', form=form,
                               employee='')


@app.route('/read')
def read():
    all_employees = Employees.query.all()
    employees_string = ""
    for employee in all_employees:
        employees_string += "<br>" + employee.name
    return employees_string


@app.route('/update/<name>')
def update(name):
    first_employee = Employees.query.first()
    first_employee.name = name
    db.session.commit()
    return first_employee.name

@app.route('/delete')
def delete():
    employee_to_delete = Employees.query.first()
    db.session.delete(employee_to_delete)
    db.session.commit()
    return "One Name deleted from database"
