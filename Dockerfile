```# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=cac_code/app.py

CMD ["python3", "-m", "flask","--app","cac_code/app.py" "run", "--host=8.0.8.0"]```