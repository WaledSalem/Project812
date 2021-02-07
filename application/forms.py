from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BasicForm(FlaskForm):

    name = StringField('Name',
                       validators=[DataRequired()])
    answer1 = StringField('Answer1',
                          validators=[DataRequired()])
    answer2 = StringField('Answer2',
                          validators=[DataRequired()])
    answer3 = StringField('Answer3',
                          validators=[DataRequired()])
    answer4 = StringField('Answer4',
                          validators=[DataRequired()])
    answer5 = StringField('Answer5',
                          validators=[DataRequired()])
    answer6 = StringField('Answer6',
                          validators=[DataRequired()])
    answer7 = StringField('Answer7',
                          validators=[DataRequired()])
    answer8 = StringField('Answer8',
                          validators=[DataRequired()])
    answer9 = StringField('Answer9',
                          validators=[DataRequired()])
    answer10 = StringField('Answer10',
                           validators=[DataRequired()])
    answer11 = StringField('Answer11',
                           validators=[DataRequired()])
    answer12 = StringField('Answer12',
                           validators=[DataRequired()])
    answer13 = StringField('Answer13',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')
