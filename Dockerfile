FROM python:3.6.9

# ARG YOUR_ENV

#ENV YOUR_ENV=${YOUR_ENV} \
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6 \
  DATABASE_URL= \
  SECRET=

# System deps:
# RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
RUN pip install --upgrade pip
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Creating folders, and files for a project:
COPY . /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
 # && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
 && poetry install
