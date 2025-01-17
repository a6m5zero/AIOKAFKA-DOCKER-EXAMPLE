from random import randint

from aiokafka import AIOKafkaProducer
import asyncio


async def produce():
    producer = AIOKafkaProducer(bootstrap_servers='kafka_server:9092')
    await producer.start()
    while True:
        await asyncio.sleep(1)
        val = f"{randint(1, 100)}"
        print('sended entities-1', val)
        await producer.send(topic='entities-1', value=f'entities-1 {val}'.encode('utf-8'))
        val = f"{randint(1, 100)}"
        print('sended entities-2', val)
        await producer.send(topic='entities-2', value=f'entities-2 {val}'.encode('utf-8'))
