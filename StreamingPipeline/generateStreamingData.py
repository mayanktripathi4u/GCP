import json
import random
import time
from faker import Faker
# from datetime import date, datetime

fake = Faker()

# def json_serial(obj):
#     """JSON serializer for objects not serializable by default json code"""

#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     raise TypeError ("Type %s not serializable" % type(obj))

def generate_fake_data():
    data = {
        "customer_name": fake.name(),
        "address": fake.address(),
        "dob": fake.date_of_birth(),
        "email": fake.email(),
        "purchase_date": fake.date_time_this_month(),
        "purchase_amount": round(random.uniform(10, 1000), 2),
        "purchased_product": fake.word(),
        "order_id": fake.uuid4()
    }
    return json.dumps(data, sort_keys=True, default=str)

def generate_streaming_data():
    while True:
        yield generate_fake_data()
        time.sleep(1)  # Adjust the sleep time as per your requirement

# Example usage:
# for data in generate_streaming_data():
#     print(data)


print(generate_fake_data())

