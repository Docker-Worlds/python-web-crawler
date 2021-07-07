# Dockerfile, Image, Container
FROM python

RUN apt-get -y update

RUN apt-get install -y google-chrome-stable

RUN apt-get install -y google-chrome-stable

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "python", "./app/main.py" ]