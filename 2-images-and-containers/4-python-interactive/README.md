# Python Interactive

## Commands

```sh
sudo docker build -t image_name .

# Run the container with interactive terminal mode.
sudo docker run -it image_name

# Automatically remove the container when it exists.
sudo docker run -it --rm image_name

# Restart the container with attached and interactive mode.
sudo docker start -ai container_id_or_name
```

## Note

```sh
sudo docker start -a container_id_or_name
```

- The above command does not allow entering inputs as it is just meant to attach the container.
