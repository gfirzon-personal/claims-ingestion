https://pypistats.org/packages/confluent-kafka

To see the list of topics in kafka:
```sh
docker exec -it kafka kafka-topics.sh --list --bootstrap-server localhost:9092
```

i need to run kafka inside a docker container on windows 11. 
I already have bitnami/kafka image downloaded. What is the docker run command to launch it?