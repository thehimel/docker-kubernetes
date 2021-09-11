# Create a container by fetching python docker image from docker hub.
FROM python

# Change working directory to /src in the container.
WORKDIR /src

# Copy all the files from current directory of host machine to the /app of the container.
COPY . /src

# Execute this command during the creation of the container
RUN pip install -r /src/requirements.txt

# Execute "python script.py" when container starts
CMD ["python", "/src/app"]
