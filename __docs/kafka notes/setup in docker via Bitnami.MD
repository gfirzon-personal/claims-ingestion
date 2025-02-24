If you prefer a simpler setup (without ZooKeeper), use Bitnami's Kafka image, which doesn't require a separate ZooKeeper service:

```sh
docker run -d --name kafka -p 9092:9092 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest
```

Then test Kafka:

### List existing topics
```sh
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --list
```

Check Container Logs
```sh
docker logs kafka
```

```sh
docker network create kafka-network
docker network create kafka-net
```

### Run kafka (with no volume) - Verified!!!
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
  bitnami/kafka
```

```sh
docker stop kafka
docker rm kafka
```sh

$HOST_IP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -like "*Ethernet*" -or $_.InterfaceAlias -like "*Wi-Fi*" }).IPAddress
echo $HOST_IP

172.17.32.1
172.26.96.1
192.168.4.43