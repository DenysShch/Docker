FROM python:3.4.5-slim

RUN mkdir /opt/hello_app

WORKDIR /opt/hello_app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

EXPOSE 5000

ENV FLASK_APP=flask_docker.py

CMD ["flask", "run", "--host", "0.0.0.0"]