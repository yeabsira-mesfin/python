from threading import *
def display():
    for i in range(1,11):
        print("Child Thread")

# t = Thread(target = display)
# t.start()
# for i in range(1,11):
#     print("Main Thread: ")
def show():
    for i in range(1,11):
        print("Grant Child Thread")
        
if __name__ == "__main__":
    t = Thread(target=display)
    t.start()
    t1 = Thread(target = show)
    t1.start()
    for i in range(1,11):
        print("Main Thread")