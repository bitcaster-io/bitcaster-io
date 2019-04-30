FROM python:3.6.8-alpine3.8 as base

WORKDIR /app

RUN pip install flask bootstrap-flask
ADD /src /code
WORKDIR /code

ENTRYPOINT ["python"]
CMD ["app.py"]

