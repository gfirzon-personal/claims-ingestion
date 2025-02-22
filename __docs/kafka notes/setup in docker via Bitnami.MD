If you prefer a simpler setup (without ZooKeeper), use Bitnami's Kafka image, which doesn't require a separate ZooKeeper service:

```sh
docker run -d --name kafka -p 9092:9092 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest
```

Then test Kafka:

```sh
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --list
```

Check Container Logs
```sh
docker logs kafka
```

```sh
docker run -d --name kafka `
  -p 9092:9092 `
  -e ALLOW_PLAINTEXT_LISTENER=yes `
  -e KAFKA_ENABLE_KRAFT=yes `
  -e KAFKA_CFG_NODE_ID=1 `
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker `
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 `
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 `
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT `
  -e KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT `
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER `
  bitnami/kafka:latest
```
