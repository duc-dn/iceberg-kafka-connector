from time import time
from faker import Faker
from kafka import KafkaProducer
import json, time
import random

faker = Faker()

city = [
            "Ha Nam", "Ha Noi", "Hai Phong", "Thai Binh",
            "Ninh Binh", "Lang Son", "Thanh Hoa", "Ha Tinh",
            "Quang Binh", "Quang Tri", "Quang Ninh", "Cao Bang"
        ]
def generate_dummy_data(i: int):
    return {
        'userid': str(i),
        'name': faker.name(),
        'year': faker.year(),
        'job': faker.job(),
        'city': city[random.randint(0, len(city) - 1)],
        'salary': random.randrange(100, 2000)
    }

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=['broker:9092'],
        value_serializer=json_serializer
    )

    i = 0
    while True:
        i += 1
        user = generate_dummy_data(i)
        print(user)
        producer.send(topic='user', value=user)
        time.sleep(1)