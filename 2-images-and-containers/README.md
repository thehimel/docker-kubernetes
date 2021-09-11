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
RUN pip install -r /app/requirements.txt
CMD ["ptyhon", "script.py"]
```

- RUN is executed once the container is created.
- CMD is executed everytime the container starts.
