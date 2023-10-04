# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y libgomp1
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=cac_code/app.py

CMD ["flask","--app","cac_code/app.py", "run", "--host=0.0.0.0"]