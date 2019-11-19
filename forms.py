from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Tasks


# create a task form
class TasksForm(Form):
    year = DateField('Date', validators=[DataRequired()])
    taskname = StringField('Task', validators=[DataRequired()])
    des = StringField('Description', validators=[DataRequired()])
    state = StringField('Complete or Not', validators=[DataRequired()])


# This from was created to finish the search all tasks in one day's function
class STasksForm(Form):
    year = DateField('Date', validators=[DataRequired()])

class StudForm(Form):
    userId = StringField('Id', validators=[DataRequired()])
    stuname = StringField('name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
