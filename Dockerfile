FROM python:3.12.8

WORKDIR /home/

RUN git clone https://github.com/qjatn23/maple.git

WORKDIR /home/maple/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-j3-tvk81*f=9xx*g9!gb-44-!6_mkx6tc6uzqk" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]