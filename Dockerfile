FROM python:3.7-slim

ADD . /YAF
WORKDIR /YAF

RUN pipenv install

CMD [ "pipenv" , "run", "python", "run.py", "no-ngrok" ]