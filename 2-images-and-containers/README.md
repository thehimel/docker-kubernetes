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
