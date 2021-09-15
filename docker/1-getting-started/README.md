# Getting Started

## Run

```sh
# Build a container with the Dockerfile in the current directory.
docker build .

# List all the processes including the stopped containers.
sudo docker ps -a

# Run the container
docker run image_id

# Stop a container
docker stop container_name

# Remove a container
sudo docker rm container_id

# Remove an image
sudo docker rmi image_id
```

