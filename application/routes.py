#!/usr/bin/python3

from application import app, db
from application.models import Employees, Answers
from flask import render_template, request, redirect, url_for
from application.forms import BasicForm, ModifyForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BasicForm()
    if form.validate_on_submit():
        new_employee = Employees(name=form.name.data)
        new_answer1 = Answers(answer=form.answer1.data, question_id=1,
                              employee_id=form.name.data)
        new_answer2 = Answers(answer=form.answer2.data, question_id=2,
                              employee_id=form.name.data)
        new_answer3 = Answers(answer=form.answer3.data, question_id=3,
                              employee_id=form.name.data)
        new_answer4 = Answers(answer=form.answer4.data, question_id=4,
                              employee_id=form.name.data)
        new_answer5 = Answers(answer=form.answer5.data, question_id=5,
                              employee_id=form.name.data)
        new_answer6 = Answers(answer=form.answer6.data, question_id=6,
                              employee_id=form.name.data)
        new_answer7 = Answers(answer=form.answer7.data, question_id=7,
                              employee_id=form.name.data)
        new_answer8 = Answers(answer=form.answer8.data, question_id=8,
                              employee_id=form.name.data)
        new_answer9 = Answers(answer=form.answer9.data, question_id=9,
                              employee_id=form.name.data)
        new_answer10 = Answers(answer=form.answer10.data, question_id=10,
                               employee_id=form.name.data)
        new_answer11 = Answers(answer=form.answer11.data, question_id=11,
                               employee_id=form.name.data)
        new_answer12 = Answers(answer=form.answer12.data, question_id=12,
                               employee_id=form.name.data)
        new_answer13 = Answers(answer=form.answer13.data, question_id=13,
                               employee_id=form.name.data)
        db.session.add_all([new_employee, new_answer1, new_answer2, new_answer3,
                            new_answer4, new_answer5, new_answer6, new_answer7,
                            new_answer8, new_answer8, new_answer9, new_answer10,
                            new_answer11, new_answer12, new_answer13])
        db.session.commit()
        return render_template('home.html', form=form,
                               employee=new_employee)
    else:
        return render_template('add.html', form=form, employee='')


@app.route('/read', methods=['GET', 'POST'])
def read():
    heading = ('ID', 'Answer', 'Question ID', 'Employee ID')
    all_answers = Answers.query.all()
    answer = Answers.id
    return render_template('read.html', heading=heading,
                           all_answers=all_answers, answer=answer)

@app.route('/update/<int:answer_id>', methods = ['GET', 'POST'])
def update(answer_id):
    form = ModifyForm()
    if form.validate_on_submit():
        #answer_to_update = db.session.query(Answers).filter_by(id=answer_id).first()
        answer_to_update = Answers.query.filter_by(id=answer_id).first()
        answer_to_update.answer = form.answer.data
        db.session.commit()
        return redirect('/read')
    else:
        return render_template('update.html', form=form)

@app.route('/delete/<int:answer_id>', methods = ['GET', 'POST'])
def delete(answer_id):
    answer_to_delete = Answers.query.filter_by(id=answer_id).first()
    db.session.delete(answer_to_delete)
    db.session.commit()
    return redirect('/read')
