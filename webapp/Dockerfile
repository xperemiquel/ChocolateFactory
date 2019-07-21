FROM python:3.6
LABEL Willy Wonka Chocolate Factory

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r /code/requirements.txt

ADD . /code/

