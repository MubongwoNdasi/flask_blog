from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    input_string = StringField('Make request', validators=[DataRequired()])
    submit = SubmitField('Request')
