# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.13

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install production dependencies.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT -w 1 -k eventlet run:app
