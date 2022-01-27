FROM python:latest

RUN pip install jinja2

COPY . .
RUN pwd && ls -Al
CMD [ "python", "/generator.py" ]
