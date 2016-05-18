FROM python:2.7.8

RUN mkdir -p /usr/src/quick_flask
WORKDIR /usr/src/quick_flask
COPY . /usr/src/quick_flask

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","quick_flask.py"]