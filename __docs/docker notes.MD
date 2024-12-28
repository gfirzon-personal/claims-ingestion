docker build -t claims-injestion-image .

docker run --name claims-injestion-container -p 8000:8000 claims-injestion-image