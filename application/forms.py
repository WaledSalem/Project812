from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BasicForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    answer1 = StringField('Answer',
                          validators=[DataRequired()])
    answer2 = StringField('Answer',
                          validators=[DataRequired()])
    answer3 = StringField('Answer',
                          validators=[DataRequired()])
    answer4 = StringField('Answer',
                          validators=[DataRequired()])
    answer5 = StringField('Answer',
                          validators=[DataRequired()])
    answer6 = StringField('Answer',
                          validators=[DataRequired()])
    answer7 = StringField('Answer',
                          validators=[DataRequired()])
    answer8 = StringField('Answer',
                          validators=[DataRequired()])
    answer9 = StringField('Answer',
                          validators=[DataRequired()])
    answer10 = StringField('Answer',
                           validators=[DataRequired()])
    answer11 = StringField('Answer',
                           validators=[DataRequired()])
    answer12 = StringField('Answer',
                           validators=[DataRequired()])
    answer13 = StringField('Answer',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')
