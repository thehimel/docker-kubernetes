# Docker Images and Containers

## 3 Run External Images

```sh
# Pull the latest python image.
sudo docker pull python

# Run with interactive terminal
sudo docker run -it python
```

## 5 Build Image with Dockerfile

### RUN vs. CMD

```sh
RUN pip install -r /src/requirements-dev.txt
CMD ["ptyhon", "script.py"]
```

- RUN is executed once during the creation of the image.
- CMD is executed everytime the container starts.
- CMD is generally the last line of a Dockerfile.
- If no ENTRYPOINT is defined, CMD is the ENTRYPOINT.

## 6 Run Container from Image

#### Publish Ports

```dockerfile
# Run the service on PORT 80 of the container.
EXPOSE 80
```

```sh
# p=publish | HOST_PORT:CONTAINER_PORT
docker run -p 3000:80 image_id
```

## 8 Image Layers

- For every line of instruction mentioned in the Dockerfile, an image is created.
This is referred as the layered architecture of the image.
- An image is created and cached at every step. If no change is detected,
the cached version will be used during the re-creation of the image from the Dockerfile.
- For optimization, we copy the dependency file that doesn't often change, install it, and then copy the source code
and tests. Thus, a cached image is created after the installation of the dependencies. And when we change the source
code, the cached version of the dependency installation image can be used. It makes the execution faster.

## 11 Restart Containers

```sh
# List all containers including the stopped containers.
sudo docker ps -a

# Restart a stopped container
sudo docker start container_name

# Stop a running container
sudo docker stop container_name
```

## 12 Attached and Detached Containers

- Attached Mode: Runs the container in foreground.
- Detached Mode: Runs the container in background.
- When we run a container, it executes in attached mode by default.
- When we restart a container, it executes in detached mode by default.

```sh
# Run a container in detached mode.
sudo docker run -d -p 5000:5000 docker-flask

# Attach a detached container.
sudo docker container attach container_id_or_name

# Restart a container in attached mode.
sudo docker start -a container_id_or_name

# Print the logs of a detached container
sudo docker logs container_id_or_name

# Follow log output of a detached container
sudo docker logs -f container_id_or_name
```

## 13 Enter Interactive Mode

Used for mostly utility apps. Not recommended for web apps.

### Commands

```sh
# Run the container with interactive terminal mode.
sudo docker run -it image_name

# Restart the container with attached and interactive mode.
sudo docker start -ai container_id_or_name
```

### Note

```sh
sudo docker start -a container_id_or_name
```

- The above command does not allow entering inputs as it is just meant to attach the container.

## 14 Delete Images and Containers

- We can only remove a stopped container.
- We can only remove an image if it is not used by any stopped or running container.

```sh
# Remove a container
sudo docker rm container_name_or_id

# Remove multiple container
sudo docker rm container1 container2 container3

# Remove all stopped containers
sudo docker prune

# Remove an unused image
sudo docker rmi image_name_or_id

# Remove multiple unused images
sudo docker rmi image1 image2

# Remove all unused images
sudo docker image prune
```

## 15 Remove Stopped Containers

```sh
# Automatically remove the container when it exists with --rm.
sudo docker run --rm image_name
```

## 16 Inspect Images

Inspect an image to get various information such as id, date_created, working_dir, entrypoint, author, os, layers, etc.

```sh
# Inspect an image
sudo docker image inspect image_name

# Inspect the python image
sudo docker image inspect python
```

## 17 Copy Files

```sh
# Copy a directory from local machine to the container
docker cp mydir container_name:/condir

# Copy a file from local machine to the container
docker cp mydir/file.txt container_name:/condir

# Copy a directory from container to the local machine
docker cp container_name:/condir mydir

# Copy a file from container to the local machine
docker cp container_name:/condir/file.txt mydir
```

- Note: A file that is being executed cannot be replaced.
