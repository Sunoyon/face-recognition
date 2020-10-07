FROM python:3.7.5-stretch

COPY . /opt/app
WORKDIR /opt/app
RUN pip3 install -r requirements.txt
