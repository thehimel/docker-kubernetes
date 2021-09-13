# Data Management and Volumes

## 2 Kinds of Data

Kinds of Data
- Application (Code + Environment)
- Temporary App Data (e.g. entered user input)
- Permanent App Data (e.g. user accounts)

## 8 Named Volumes

- Volumes are managed by Docker.
- Can be managed with `docker volume`. Parameters: `ls` = list, `rm` = remove, `prune` = remove all unused volumes.
- Volume Types
  - Anonymous (Non-Persistent)
    - Automatically gets removed from the local machine when container exits.
    - Docker sets a path on the host machine which is deleted when container exits. Exact location is unknown.
    - Cannot be shared across containers.
  - Named (Persistent)
    - Persists even after the container exits.
    - A directory is created inside the container which is not deleted when container exits.
    - Make sure that the directory or the parent of the directory in local machine is accessible by Docker.
    - Can be shared across containers.
    - `sudo docker run -v local_path:container_path image_name`
    - `sudo docker run -v feedback:/app/feedback image_name`

## 9 Bind Mounts

https://docs.docker.com/storage/bind-mounts/

### Bind Mounts

- Mounts a local directory to a path in the container.
- No directory is created inside the container.
- Can be used for edit-prone src code.
- The absolute path of the local machine should be passed.
- All the files of `container_path` is removed and the `local_path` is mounted to the container_path.
- `sudo docker run -v /home/absolute/local_path:container_path image_name`
- `sudo docker run -v /home/project-name:/app image_name`
- Now, if the source code updates, the image shouldn't be rebuilt. Only restarting the container will fetch the updates.

### Node Modules

- Node needs the `node_modules` directory to run the app which is initially installed.
- But during the bind mount step, `container_path/node_modules` gets deleted.
- We can make use of `Anonymous Volume` to make the consistent-prone files persistent.
- `sudo docker run -v /home/absolute/local_path:container_path -v /container_path/node_modules image_name`
- `sudo docker run -v /home/project-name:/app -v /app/node_modules image_name`
- Here `-v /container_path/node_modules` refers to the `Anonymous Volume`.
- We can also define `Anonymous Volume` as `VOLUME ["/app/node_modules]` in the Dockerfile.
- Now, during the bind mount step, `container_path/node_modules` does not get deleted.
- Named volume, bind mound, anonymous volume at once.
  - `sudo docker run -v feedback:/app/feedback -v /home/project-name:/app -v /app/node_modules image_name`
  - Docker understands the related local path as the named volume, absolute local path as the bind mound,
  and anonymous volume has only container path.

## 11 Nodemon

- It doesn't restart the server automatically when the source code is updated.
- Thus, `nodemon` is added as a dependency which restarts the server automatically when the source code is updated.
- Flask apps can also be configured to restart the server when source code is updated.
- Now, whenever the mounted source code is updated, the server restarts.
