To install Azurite that is to be run from Docker
```sh
docker pull mcr.microsoft.com/azure-storage/azurite
```

Create a named volume:
```sh
docker volume create azurite_volume
```

Run Azurite with the volume:
```sh
docker run -d --name azurite -p 10000:10000 -p 10001:10001 -p 10002:10002 -v azurite_volume:/workspace mcr.microsoft.com/azure-storage/azurite
```

Verify the Container is Running
```sh
docker ps
```

Stopping & Restarting Azurite
To stop the container:
```sh
docker stop azurite
```
To restart the container:
```sh
docker start azurite
```

To remove the container (without deleting stored data):
```sh
docker rm azurite
```

To remove the container and delete all stored data:
```sh
docker rm -v azurite
```
