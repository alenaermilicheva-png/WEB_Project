from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class EventForm(FlaskForm):
    title = StringField('Название события', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    date = StringField('Дата и время', validators=[DataRequired()])
    location = StringField('Место проведения', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    max_volunteers = IntegerField('Нужно волонтеров', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Создать событие')