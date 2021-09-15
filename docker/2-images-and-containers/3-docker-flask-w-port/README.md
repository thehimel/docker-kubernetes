# Docker Flask with Port

## Commands

```sh
sudo docker build -t docker-flask .
sudo docker run -d -p 5000:5000 docker-flask
```

## Note

- The app is accessible at http:127.0.0.1:5000.
- Use `boot2docker ip`, if you're using boot2docker.
