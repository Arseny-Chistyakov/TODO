# из-за неправильной иниц. репозитория данный dockerfile для backend лежит тут
from python:3.10.7

RUN pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install gunicorn
