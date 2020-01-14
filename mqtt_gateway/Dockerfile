FROM python:3.7-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY ./src .

COPY config.docker.json ./config.json

CMD [ "python", "main.py", "config.json" ]
