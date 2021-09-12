# Data Management and Volumes

## 2 Kinds of Data

Kinds of Data
- Application (Code + Environment)
- Temporary App Data (e.g. entered user input)
- Permanent App Data (e.g. user accounts)

## 8 Named Volumes

- Volumes are managed by Docker.
- Can be managed with `docker volume`. Parameters: `ls` = list, `rm` = remove, `prune` = remove all unused volumes.
- Types of Volumes
  - Anonymous Volumes (Non-Persistent)
    - Docker sets a path on the host machine. Exact location is unknown.
    - Automatically gets removed from the local machine when container exists.
  - Named Volumes (Persistent)
    - Persists even after the container exists.
    - `sudo docker run -v local_path:container_path image_name`
    - `sudo docker run -v feedback:/app/feedback image_name`
