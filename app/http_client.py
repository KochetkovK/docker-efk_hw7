import requests
import random

url_part = ('one', 'two', 'three', 'four', 'five', 'error')
for _ in range(1000):
    rand_part = random.choice(url_part)
    requests.get(f"http://0.0.0.0:5000/{rand_part}")

