# LAB - Class 31

Project: Use Django REST Framework to create an API, then “containerize” it with Docker.

Author: Andrea Riley(Thiel)

## Feature Tasks and Requirements

### Django REST Framework

Rebuild a custom version of Things API demo project from scratch. *completed 02-19-2024 10:00PM EST*

- Replace things_project and Thing with your own application and model.
- Your model must have at least as many fields as demo’s model.
- Your model must have one field that is a foreign key to user.
- **NOTE:** You are not required to build any templates for this lab.

### Docker

*completed 02-20-2024 5:00PM EST*

**NOTE** Refer to the class demo for built out Dockerfile and docker-compose.yml examples.

Update Dockerfile and docker-compose.yml if needed.

## Links and Resources

back-end server url (when applicable)
front-end application (when applicable)

## Setup

.env requirements

  .venv

  PORT - 8000

  DATABASE_URL- /api/v1/plants/


Initialize/run your application

  python manage.py runserver

How to use your library

  pip install -r requirements.txt

## Tests

How to run tests

  python manage.py tests
