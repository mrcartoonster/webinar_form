from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class WebinarForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Enter first name'), Length(max=20)])
    submit = SubmitField('Submit')