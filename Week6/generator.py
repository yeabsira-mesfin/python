def my_gen():
    n = [100,200,300]
    print('This is printed first')

    yield n

    n.append(400)
    print('This is printed second')
    yield n

    n.append(500)
    print('This is printed at last')
    yield n
    
for item in my_gen():
    print(item)   
    
def addgen():
    n=1
    print("First")
    
    n +=1
    yield n
    
    print("second")
    n +=1
    yield n
    
    
for i in addgen():
    print(i)