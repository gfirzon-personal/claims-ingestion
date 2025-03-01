### Build Docker image to be used as base image
```sh
docker build -t claims-injestion-image-base:latest -f Dockerfile-base . 
```

### Build Docker final image
```sh
docker build -t claims-injestion-image .
```

Run the docker container using the image
```sh
docker run --name claims-injestion -p 8000:8000 claims-injestion-image
```