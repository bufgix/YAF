FROM python:3.7-slim

ADD . /YAF
WORKDIR /YAF

RUN pip install pipenv
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "run.py" ]
