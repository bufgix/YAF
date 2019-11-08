FROM python:3.7-slim

ADD . /YAF
WORKDIR /YAF

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "run.py" ]
