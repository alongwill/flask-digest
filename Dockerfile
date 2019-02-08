FROM python:3.7.2-alpine3.9

COPY ./ ./app
WORKDIR ./app

RUN pip install flask
CMD python server.py
