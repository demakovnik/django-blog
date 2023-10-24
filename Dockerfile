FROM python:3.10.2-slim
ENV PYTHONBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
COPY ./code/ /code
WORKDIR /code/django_blog
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000