''' Forms '''
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    ''' Validation for the message form '''
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    