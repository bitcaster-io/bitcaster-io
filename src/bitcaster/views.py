from collections import OrderedDict

from flask import make_response, render_template, request
from flask_mail import Message

from bitcaster.app import app, mail
from bitcaster.forms import ContactForm


@app.route('/')
def home():
    r = make_response(render_template('index.html'))
    return r


@app.route('/dispatchers/')
def dispatchers():
    plugins = {'facebook': 'Facebook',
               'gmail': 'GMail',
               'hangout': 'Hangout',
               'plivo': 'SMS (Plivo)',
               'skype': 'Skype',
               'slack': 'Slack',
               'telegram': 'Telegram',
               'twilio': 'SMS (Twilio)',
               'twitter': 'Twitter',
               'viber': 'Viber',
               'whatsapp': 'Whatsapp',
               'yammer': 'Yammer',
               'zulip': 'Zulip'
               }
    r = make_response(render_template('dispatchers.html', plugins=plugins))
    return r


@app.route('/info/', methods=('GET', 'POST'))
def info():
    form = ContactForm(release=request.args.get('release'))
    ctx = {"form": form}
    if request.method == 'POST':
        if form.validate_on_submit():
            body = """
Release: {release}    
First Name: {first_name}
Last Name: {last_name}
Email: {email}
Phone: {phone}
Company: {company}
Web Site: {company_website}
Note:{use_case}
            """.format(**form.data)
            msg = Message("Contact request",
                          body=body,
                          sender='s.apostolico@gmail.com',
                          recipients=app.config['MAIL_RECIPIENTS'].split(','))
            try:
                mail.send(msg)
                ctx['email_sent'] = True
            except ConnectionRefusedError:
                ctx['ConnectionRefusedError'] = True

    r = make_response(render_template('info.html', **ctx))
    return r


@app.route('/offers/')
def pricing():
    features = OrderedDict()
    features['General features'] = [
        ('Unlimited users', False, True, True),
        ('View events across all applications in your organization', False, False, True),
        ('Third-party integrations', False, False, True)]

    features['Monitoring & Management'] = [
        ('Configurable notification logging level', False, True, True),
        ('Extended time series data', False, True, True),
        ('Custom rate limits on a per-application basis', False, False, True),
        ('Custom rate limits on a per-events basis', False, False, True)]

    features['Security & Administration'] = [
        ('Single-sign-on via Google Apps and GitHub Organizations', False, True, True),
        ('Single-sign-on via Microsoft Azure ', False, False, True),
        ('LDAP Authentication', False, False, True),
        ('Two-factor authentication via U2F device, TOTP app, or SMS', False, True, True)]

    features['Support and Services'] = [
        ('Community forum access', True, True, True),
        ('Multiple language messages', False, True, True),

        ('Priority support and custom support agreement', '-'),
        ('Private onboarding and training sessions', '-')]

    r = make_response(render_template('offers.html', features=features))
    return r


@app.route('/<page>/')
def page(page):
    r = make_response(render_template('%s.html' % page))
    return r

#
# @app.route('/vendor/<path:path>')
# def send_js(path):
#     return send_from_directory('vendor', path)
