from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class EventForm(FlaskForm):
    title = StringField('Название события', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    date = DateTimeField('Дата и время (ГГГГ-ММ-ДД ЧЧ:ММ)', validators=[DataRequired()], format='%Y-%m-%d %H:%M')
    location = StringField('Место проведения', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    max_volunteers = IntegerField('Нужно волонтеров', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Создать событие')