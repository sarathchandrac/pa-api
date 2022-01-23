FROM python:3.7-alpine
LABEL maintainer="csc111vs@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app
# run the application using new user instead of root user
RUN adduser -D user

USER user
