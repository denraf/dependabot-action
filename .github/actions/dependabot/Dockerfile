FROM python:latest
ARG exclude-dir
ENV env_exclude_dir=$exclude-dir
RUN pip install jinja2

COPY . .
CMD [ "python", "/generator.py" ]
