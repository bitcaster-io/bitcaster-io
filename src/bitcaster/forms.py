from flask import request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea, HiddenInput


class ContactForm(FlaskForm):
    release = StringField('Release', widget=HiddenInput())
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()], )
    email = StringField('Email', validators=[Email()])
    phone = StringField('Phone Number', validators=[],
                        render_kw={"placeholder": "optional"})
    company = StringField('Company', validators=[InputRequired()])
    company_website = StringField('Company Site', validators=[])
    use_case = StringField('', widget=TextArea(),
                           render_kw={"placeholder": "describe here your use case"})
    recaptcha = RecaptchaField()
