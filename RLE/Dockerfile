FROM python:2.7

ADD . /app/src

WORKDIR /app/src

RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]
