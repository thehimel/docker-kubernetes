# Docker Flask

Source: https://docs.docker.com/language/python/build-images/

## Commands

```sh
sudo docker build . --tag python-docker
sudo docker run python-docker
sudo docker images
sudo docker tag python-docker:latest python-docker:v1.0.0
sudo docker rmi python-docker:v1.0.0
```
