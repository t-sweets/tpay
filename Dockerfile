FROM python:3.6.5

ARG project_dir=/app/

ADD requirements.txt $project_dir

WORKDIR $project_dir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
