FROM python:3.7-alpine

MAINTAINER Andy Feetenby

# Recommended when running python in Docker
ENV PYTHONUNBUFFERED 1

# Copies files containing dependencies
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app

RUN adduser -D user
USER user