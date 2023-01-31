# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

RUN pip install --upgrade pip


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY ../../requirements.txt .
RUN pip install -r requirements.txt

COPY .. ./app

CMD [ "python3", "./app/app.py"]