# Create a container by fetching python docker image from docker hub.
FROM python

# Change working directory to /app in the container.
WORKDIR /app

# Copy all the files from current directory of host machine to the /app of the container.
COPY . /app

# Run "python script.py"
CMD [ "python", "script.py" ]
