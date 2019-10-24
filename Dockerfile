FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install pipenv
COPY Pipfile .
RUN pipenv install --system --skip-lock
COPY ./ .
