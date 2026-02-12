from threading import *
from time import *
def holla():
    print(ctime())
    Timer(1,holla).start()
    
holla()