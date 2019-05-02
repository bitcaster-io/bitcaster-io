FROM python:3.6.8-alpine3.8

WORKDIR /app
ENV FLASK_APP "bitcaster.app"
ENV BOOTSTRAP_USE_MINIFIED "1"
ENV BOOTSTRAP_SERVE_LOCAL "1"
ENV BOOTSTRAP_QUERYSTRING_REVVING "1"
ENV RECAPTCHA_PUBLIC_KEY ""
ENV RECAPTCHA_PRIVATE_KEY ""
ENV MAIL_SERVER ""
ENV MAIL_PORT ""
ENV MAIL_USE_TLS ""
ENV MAIL_USE_SSL ""
ENV MAIL_DEBUG ""
ENV MAIL_USERNAME ""
ENV MAIL_PASSWORD ""
ENV MAIL_DEFAULT_SENDER ""
ENV MAIL_MAX_EMAILS ""
ENV MAIL_SUPPRESS_SEND ""
ENV MAIL_ASCII_ATTACHMENTS ""
ENV SECRET_KEY ""

ADD /src /code
ADD Pipfile.lock /code
ADD Pipfile /code
WORKDIR /code

RUN pip install pipenv \
    && pipenv install --verbose --system --deploy --ignore-pipfile

#ENTRYPOINT ["python"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "bitcaster.wsgi:app"]

