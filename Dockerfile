# base image
FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install pipenv
RUN pip install pipenv

# copy Pipfile and Pipfile.lock
COPY Pipfile* /app/

# install dependencies
RUN pip install pipenv && pipenv install --system --dev


# copy project
COPY . /app/

# run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
