import asyncio
import random

from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer('entities-1', group_id=f'entities_consumer_1' , bootstrap_servers='kafka_server:9092')
    await consumer.start()
    print('consumer started')
    async for msg in consumer:
        print(msg.value.decode('utf-8'), msg.topic, msg.partition, msg.offset)
        await asyncio.sleep(0.5)
