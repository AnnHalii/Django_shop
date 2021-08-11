FROM python:3.8-slim as base

ENV PYTHONUNBUFFERED 1
RUN mkdir /shop
WORKDIR /shop
COPY requirements.txt /shop/
RUN pip install -r requirements.txt

FROM base as dev
COPY . /shop/