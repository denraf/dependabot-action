FROM python:latest

RUN pip install jinja2

COPY . .
RUN pwd && ls -Al /home
CMD [ "python", "/generator.py" ]
