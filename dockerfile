FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /catalogo
WORKDIR /catalogo
ADD . /catalogo/
RUN pip install -r requirements.txt

EXPOSE 8081
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT