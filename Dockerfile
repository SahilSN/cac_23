# syntax=docker/dockerfile:1

FROM python:3.7-alpine

WORKDIR /python-docker
ENV FLASK_APP=cac_code/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y libgomp1
RUN pip3 install pandas
RUN pip3 install -r requirements.txt
EXPOSE 5000

COPY . .

CMD ["flask","--app","cac_code/app.py", "run"]
