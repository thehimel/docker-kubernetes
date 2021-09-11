# Create a container by fetching python docker image from docker hub.
FROM python

# Change working directory in the container.
WORKDIR /app

# Copy the files that are not often changed to take advantage of the layered architecture of the docker images.
COPY requirements-dev.txt /app
COPY requirements-test.txt /app

# Execute these command during the creation of the image
RUN pip install -r /app/requirements-dev.txt
RUN pip install -r /app/requirements-test.txt

# Copy all the files from current directory of host machine to the working directory of the container.
COPY . /app

RUN pytest /app/tests

# Execute this command when container starts
CMD ["python", "-m", "src"]
