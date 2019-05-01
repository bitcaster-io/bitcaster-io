import os
from pathlib import Path

from flask import Flask, make_response, send_from_directory
from flask import render_template
from flask_bootstrap import Bootstrap
from jinja2 import Markup

here = Path(__file__).parent

app = Flask(__name__)


@app.template_filter()
def checkmark(on_off):
    """Convert a string to all caps."""
    if on_off:
        value = '<i class="fas fa-check green mr-2"></i>'
    else:
        value = ''
    return Markup(value)


@app.context_processor
def globals():
    return dict(GOOGLE_ANALYTICS_CODE=os.environ.get('GOOGLE_ANALYTICS_CODE', None),
                )


bootstrap = Bootstrap(app)


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


@app.route('/pricing/')
def pricing():
    features = [('View events across all projects in your organization', False, False, True),
                ('Third-party integrations', False, False, True),
                ('Configurable notification logging level', False, True, True),

                ]
    r = make_response(render_template('pricing.html', features=features))
    return r


@app.route('/<page>/')
def page(page):
    r = make_response(render_template('%s.html' % page))
    return r


@app.route('/vendor/<path:path>')
def send_js(path):
    return send_from_directory('vendor', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
