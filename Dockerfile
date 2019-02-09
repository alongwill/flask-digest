FROM python:3.7.2-alpine3.9

RUN pip install flask

EXPOSE 5000

COPY ./ ./app
WORKDIR ./app

ENTRYPOINT [ "python", "server.py" ]
