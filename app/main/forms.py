from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TextForm(FlaskForm):
    text = StringField("Input:", [DataRequired()])
    submit = SubmitField('Submit')
