FROM python:3.6.5

ENV PYTHONUNBUFFERED 1
ARG project_dir=/app/

# Install Requirements
ADD requirements.txt $project_dir
WORKDIR $project_dir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . $project_dir

COPY docker-entrypoint.sh /usr/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uwsgi", "--socket", ":8000", "--module", "mysite.wsgi"]
