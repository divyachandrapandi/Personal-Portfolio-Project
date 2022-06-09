from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,TextAreaField
from wtforms.validators import DataRequired,  Email

class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone = StringField("Mobile Number", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    send = SubmitField("Send")