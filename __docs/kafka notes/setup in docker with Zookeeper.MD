Kafka relies on Apache ZooKeeper, so you'll need to run both services. The easiest way is to use Docker Compose.

1. Create a docker-compose.yml file <br>
    Create a new file named docker-compose.yml (sibling file)

2.  Start Kafka & ZooKeeper <br>
    Open PowerShell or Command Prompt and navigate to the directory containing docker-compose.yml, then run:

    ```sh
    docker-compose up -d
    ```

3.  Verify the Installation <br>    
    Check running containers:
    ```sh
    docker ps
    ```

    Test Kafka:
    ```sh
    docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --list
    ```



