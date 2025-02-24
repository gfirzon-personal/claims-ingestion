Build Docker image
```sh
docker build -t claims-injestion-image .
```

Run the docker container using the image
```sh
docker run --name claims-injestion-container -p 8000:8000 claims-injestion-image
```

Run the docker container using the image and specified docker network
```sh
docker run --name claims-injestion-container --network kafka-net -p 8000:8000 claims-injestion-image
```