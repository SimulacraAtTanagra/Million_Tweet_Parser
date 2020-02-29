FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install requests
RUN pip install sodapy

