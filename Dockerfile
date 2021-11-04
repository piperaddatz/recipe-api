FROM python:3.7-alpine
MAINTAINER London App Developer Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app


RUN adduser -D user
USER user