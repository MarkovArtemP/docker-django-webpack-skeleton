FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD ../../../project /app/
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic -v 0 --clear --noinput
ADD ./uwsgi.ini
ENTRYPOINT /usr/bin/uwsgi --ini /app/docker/production/web/uwsgi.ini
