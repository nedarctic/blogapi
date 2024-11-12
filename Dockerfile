# Pull base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=blogapi_project.settings

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/

# Set entrypoint for Gunicorn
ENTRYPOINT [ "gunicorn", "blogapi_project.wsgi:application", "-b", "0.0.0.0:8000" ]
