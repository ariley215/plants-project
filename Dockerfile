FROM python:3.11.5-slim-bullseye

# Set the working directory
WORKDIR /code

#Set the environment variables
ENV PIP_DIABLE_PIP-VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

