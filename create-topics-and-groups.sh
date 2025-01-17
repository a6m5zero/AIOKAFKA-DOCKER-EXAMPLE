#!/bin/bash

# Создание топиков
/usr/bin/kafka-topics --create --topic entities --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
/usr/bin/kafka-topics --create --topic entities2 --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

# Создание групп консьюмеров
/usr/bin/kafka-consumer-groups --bootstrap-server localhost:9092 --create --group entities-group
/usr/bin/kafka-consumer-groups --bootstrap-server localhost:9092 --create --group entities2-group
