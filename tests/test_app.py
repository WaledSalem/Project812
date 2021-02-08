#!/usr/bin/python3
import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Questions, Employees, Answers

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY')
                #DEBUG=True
        return app

    def setUp(self):
        db.create_all()
        sample1 = Questions(id=1, question='What?')
        sample2 = Employees(name='John Doe')
        sample3 = Answers(id=1, answer='1', question_id=1, employee_id='John Doe')
        db.session.add(sample1)
        db.session.commit()
        db.session.add(sample2)
        db.session.commit()
        db.session.add(sample3)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

#sample3 = Answers(id=1, answer='1', question_id=1, employee_id='John Doe')

class TestRead(TestBase):
    def test_Read_get(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code,200)


class TestUpdate(TestBase):
    def test_update_get(self):
        response = self.client.get('/update/1')
        self.assertEqual(response.status_code,200)
    def test_get_update(self):
        response = self.client.get('/update/1')
        self.assertIn(b'1', response.data)

class TestAdd(TestBase):
    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_get(self):
        response = self.client.get(('/delete'),
                data = dict(id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 404)
