FROM python:3.7-slim

ADD . /YAF
WORKDIR /YAF

RUN pipenv install
RUN pipenv run python setupadmin.py

CMD [ "pipenv" , "run", "python", "run.py", "no-ngrok" ]