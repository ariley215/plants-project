# LAB - Class 32

Project: Let’s move our API closer to production grade by adding Authentication and switching to a Production Server

Author: Andrea Riley(Thiel)

## Feature Tasks and Requirements

### Django REST Framework

Add JWT Authentication to your API.

- Install needed libraries in project configuration and/or site settings.

Keep any pre-existing authentication so DRF Browsable API still usable.

- Install needed libraries in project configuration and/or site settings.

### Docker

Switch to using Gunicorn instead of Django’s built in development server.

- mind the number of workers to avoid sluggishness

**Warning** You will run into styling issues when you switch over to Gunicorn.

- On Django side you’ll need to properly handle static files using Whitenoise


## Links and Resources

<http://0.0.0.0:8000/api/v1/plants/>

## Setup

.env requirements

  .venv

  PORT - 8000

  DATABASE_URL- /api/v1/plants/

Initialize/run your application

  python manage.py runserver

   docker compose up

How to use your library

  pip install -r requirements.txt

## Tests

How to test manually:

