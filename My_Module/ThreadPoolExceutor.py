
import random

from concurrent.futures import ThreadPoolExecutor
import time
def study():
    for i in range(5):
        print("I like reading")
        time.sleep(random.random())
def listening():
    for i in range(5):
        print("Listening to music")
        time.sleep(random.random())
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(study)
        pool.submit(listening)