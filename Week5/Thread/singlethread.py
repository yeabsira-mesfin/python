from threading import *
import time
def test(n):
    i=1
    while i<=n:
        print(f" Main Thread {i}")
        i = i+1
        time.sleep(1)

if __name__ == "__main__":
    t1 = Thread(target = test,args =(6,))
    t1.start()
    t1.join()