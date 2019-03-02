FROM python:3.6.5

ENV PYTHONUNBUFFERED 1

ARG project_dir=/app/

ADD requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . $project_dir
