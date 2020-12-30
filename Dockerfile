FROM python:3.6.12-alpine3.12
RUN apk add ffmpeg py3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT FLASK_APP=zootube.py flask run --host=0.0.0.0
