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
