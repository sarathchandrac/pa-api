FROM python:3.7-alpine
LABEL maintainer="csc111vs@gmail.com"

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
# RUN mkdir /app
WORKDIR /app
RUN pwd
COPY ./app/ /app

# run the application using new user instead of root user
RUN adduser -D user

USER user
