import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_QUERYSTRING_REVVING = True
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TLS'))
    MAIL_USE_SSL = bool(os.environ.get('MAIL_USE_SSL'))
    MAIL_DEBUG = bool(os.environ.get('MAIL_DEBUG'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
    MAIL_RECIPIENTS = os.environ.get('MAIL_RECIPIENTS')
