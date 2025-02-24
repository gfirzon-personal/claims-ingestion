## Updated Docker Run Script for Kafka in KRaft Mode (Persistent)

```sh
docker network create kafka-net

docker volume create kafka_data

docker run -d --name kafka `
  --network kafka-net `
  -p 9092:9092 `
  -p 9093:9093 `
  -e KAFKA_CFG_NODE_ID=1 `
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker `
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 `
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 `
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER `
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT `
  -e KAFKA_CFG_LOG_DIRS=/bitnami/kafka/data `
  -e KAFKA_ENABLE_KRAFT=yes `
  -e ALLOW_PLAINTEXT_LISTENER=yes `
  -v kafka_data:/bitnami/kafka/data `
  bitnami/kafka:latest
  ```

  ### Run kafka (with volume) - In Testing stage!!!
```sh
docker run -d --name kafka --network kafka-net `
  -p 9092:9092 -p 9093:9093 `
  -e KAFKA_ENABLE_KRAFT=yes `
  -e KAFKA_CFG_NODE_ID=1 `
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker `
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 `
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER `
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 `
  -v kafka_data:/bitnami/kafka/data `
  bitnami/kafka
```