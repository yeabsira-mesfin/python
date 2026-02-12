source = [10,10,10,30,30,20,30,20,100,11,11]
target= []
for i in source:
    if i not in target:
        target.append(i)
print(target)

a = [10,20,30,20,10,50,60,40,80,50,40]
s=set(a)
l=list(s)
l.sort()
print(l)
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i, name in enumerate(color):
    if i%4 != 0 and i !=5:
        print(name,end=' ')
        
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color[1],color[2],color[3])
print(color[1:4])

