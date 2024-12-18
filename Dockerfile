FROM python:3.12.8

WORKDIR /home/

RUN echo "testing1234"

RUN git clone https://github.com/qjatn23/maple.git

WORKDIR /home/maple/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=maple.settings.deploy && python manage.py migrate --settings=maple.settings.deploy && gunicorn maple.wsgi --env DJANGO_SETTINGS_MODULE=maple.settings.deploy --bind 0.0.0.0:8000"]

