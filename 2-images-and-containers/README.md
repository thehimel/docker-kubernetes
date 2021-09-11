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
