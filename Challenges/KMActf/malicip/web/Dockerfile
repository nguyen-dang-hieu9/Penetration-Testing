FROM python:3-alpine

RUN apk update && apk add py-pip

WORKDIR /app

COPY ./src /app

RUN pip install -r requirements.txt

CMD ["gunicorn"]

