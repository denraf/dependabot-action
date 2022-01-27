FROM python:latest
ARG ARG_EXCLUDE_DIR
ENV EXCLUDE_DIR=$ARG_EXCLUDE_DIR
RUN pip install jinja2

COPY . .
CMD [ "python", "/generator.py" ]
