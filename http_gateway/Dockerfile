FROM python:3.7-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apk del .build-deps

WORKDIR /app

COPY ./src .

COPY config.docker.json ./config.json

CMD [ "python", "main.py", "config.json" ]
