FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /users
WORKDIR /users
ADD . /users/
RUN pip install -r requerimientos.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT