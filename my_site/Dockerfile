FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /shop
WORKDIR /shop
COPY requirements.txt /shop/
RUN pip install -r requirements.txt
COPY . /shop/