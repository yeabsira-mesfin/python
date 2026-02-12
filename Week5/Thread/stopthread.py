from threading import *
from time import *
def Thread_Function(running):
    while running.is_set():
        print('running')
        sleep(1)

if __name__ == '__main__':
    running = Event()
    running.set()

    thread = Thread(target=Thread_Function, args=(running,))
    thread.start()

    sleep(10)
    print('Event running.clear()')
    running.clear()

    print('Wait until Thread is terminating')
    thread.join()
    print("EXIT __main__")
