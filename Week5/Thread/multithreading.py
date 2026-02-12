from threading import *
import time

def test(n):
    i=1
    while i<=n:
        print(f"Main Thread {i}")
        i = i + 1
        time.sleep(1)

def demo(n):
    i = 1
    while i <= n:
        print(f"Child Thread {i}")
        i = i+1
        time.sleep(2)

if __name__ == "__main__":
    t1 = Thread(target = test, args=(5,))
    t2 = Thread(target = demo, args=(5,))
    t1.start()
    t2.start()

