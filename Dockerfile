FROM python:3.9.5-slim-buster

ADD . ./snekha

WORKDIR /snekha

RUN pip3 install -r requirements.txt

# EXPOSE 5003

CMD [ "python","app.py" ]