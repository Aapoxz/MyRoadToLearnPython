import time
import sys

def spam_hello_world():
    count = 0
    while count < 100:
        print("Hello, World!")
        time.sleep(0.1)
        count += 1

if __name__ == "__main__":
    spam_hello_world()