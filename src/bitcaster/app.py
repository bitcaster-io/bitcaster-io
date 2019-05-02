import os
from pathlib import Path

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_mail import Mail

here = Path(__file__).parent

app = Flask("bitcaster")
app.config.from_object('bitcaster.config.Config')

bootstrap = Bootstrap(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
mail = Mail(app)

from . import views
from . import template_utils


# app.config.update(
#     # SECRET_KEY=os.environ.get('SECRET_KEY'),
#     BOOTSTRAP_USE_MINIFIED=True,
#     BOOTSTRAP_SERVE_LOCAL=True,
#     BOOTSTRAP_QUERYSTRING_REVVING=True,
#     RECAPTCHA_PUBLIC_KEY=os.environ.get('RECAPTCHA_PUBLIC_KEY'),
#     RECAPTCHA_PRIVATE_KEY=os.environ.get('RECAPTCHA_PRIVATE_KEY'),
#     # RECAPTCHA_PARAMETERS={'hl': 'zh', 'render': 'explicit'},
#     # RECAPTCHA_DATA_ATTRS={'theme': 'dark'}
#     MAIL_SERVER=os.environ.get('MAIL_SERVER'),
#     MAIL_PORT=os.environ.get('MAIL_PORT'),
#     MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS'),
#     MAIL_USE_SSL=os.environ.get('MAIL_SERVER'),
#     MAIL_DEBUG=os.environ.get('MAIL_SERVER'),
#     MAIL_USERNAME=os.environ.get('MAIL_SERVER'),
#     MAIL_PASSWORD=os.environ.get('MAIL_SERVER'),
#     MAIL_DEFAULT_SENDER=os.environ.get('MAIL_SERVER'),
#     MAIL_MAX_EMAILS=os.environ.get('MAIL_SERVER'),
#     MAIL_SUPPRESS_SEND=os.environ.get('MAIL_SERVER'),
#     MAIL_ASCII_ATTACHMENTS=os.environ.get('MAIL_SERVER'),
#
# )
