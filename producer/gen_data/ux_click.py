from time import time
from faker import Faker
from kafka import KafkaProducer
import json, time
import random
import string

parent = [
            {
                "x": random.uniform(500, 1000),
                "y": random.uniform(500, 1000),
                "width": random.randint(50, 1000),
                "height": random.randint(50, 1000)
            }
        ]

views = ["/dashboard", "/view", "/staff", "/vnface"]

types = ["Desktop1920", "Desktop1366", "Ipad", "Smartphone", "Other"]

def id_generator(size=24, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_dummy_data(ux_click_id: int):
    return {
        "events": [
            {
                "key": "[CLY]_action",
                "count": 1,
                "segmentation": {
                    "type": "click",
                    "x": random.randint(500, 1000),
                    "y": random.randint(500, 1000),
                    "width": random.randint(1500, 2000),
                    "height": random.randint(1000, 2000),
                    "view": views[random.randint(0, len(views) - 1)],
                    "parent": parent[0],
                    "domain": "console-vnface.vnpt.vn"
                },
                "timestamp": 1672298256237,
                "hour": random.randint(4, 20),
                "dow": random.randint(1, 10)
            }
        ],
        "app_key": "5fa32bd8282b2fcdc247b68241faebffcd4ece04",
        "device_id": str(ux_click_id),
        "sdk_name": "javascript_native_web","sdk_version": "22.06.0",
        "t": 1,
        "timestamp": 1672298256238,
        "hour": random.randint(4, 20),
        "dow": random.randint(1, 10),
        "raw_html": None,
        "screen_size_type": types[random.randint(0, len(types) - 1)],
        "_id": i
    }

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=json_serializer
    )

    i = 0
    while True:
        i += 1
        ux_click = generate_dummy_data(i)
        print("============================================================")
        print(ux_click)
        producer.send(topic='user', value=ux_click)
        time.sleep(1)