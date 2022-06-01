FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -e .

WORKDIR /app/broker/api
