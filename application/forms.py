#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class BasicForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    answer1 = SelectField('When I am working, I think about nothing else.',
                          choices=[1, 2, 3, 4, 5])
    answer2 = SelectField('I get carried away by my work.',
                          choices=[1, 2, 3, 4, 5])
    answer3 = SelectField('When I am working, I forget everything else around me.',
                          choices=[1, 2, 3, 4, 5])
    answer4 = SelectField('I am totally immersed in my work.',
                          choices=[1, 2, 3, 4, 5])
    answer5 = SelectField('My work gives me a good feeling.',
                          choices=[1, 2, 3, 4, 5])
    answer6 = SelectField('I do my work with a lot of enjoyment.',
                          choices=[1, 2, 3, 4, 5])
    answer7 = SelectField('I feel happy during my work.',
                          choices=[1, 2, 3, 4, 5])
    answer8 = SelectField('I feel cheerful when I am working.',
                          choices=[1, 2, 3, 4, 5])
    answer9 = SelectField('I would still do this work, even if I received less pay.',
                          choices=[1, 2, 3, 4, 5])
    answer10 = SelectField('I find that I also want to work in my free time.',
                           choices=[1, 2, 3, 4, 5])
    answer11 = SelectField('I work because I enjoy it.',
                           choices=[1, 2, 3, 4, 5])
    answer12 = SelectField('When I am working on something, I am doing it for myself.',
                           choices=[1, 2, 3, 4, 5])
    answer13 = SelectField('I get my motivation from the work itself, and not from the reward for it.',
                           choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Submit')

class ModifyForm(FlaskForm):
    answer = SelectField('Update', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Submit')
