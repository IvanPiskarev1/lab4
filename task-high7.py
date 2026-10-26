import random 
import time 


def random_numbers():
    random.seed(time.time())

    while True:
        yield random.randint(1,100)


generator = random_numbers()

for _ in range(10):
    print(next(generator))
    