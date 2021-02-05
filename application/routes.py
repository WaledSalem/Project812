#!/usr/bin/python3

from application import app, db

from application.models import Employees, Questions

@app.route('/add')
def add():
    new_employee = Employees(name='Waled', question_id=1, answer='yes')
    db.session.add(new_employee)
    db.session.commit()
    return 'new employee added to database!'

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
