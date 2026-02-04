from Parent import *
class Child(Parent):
    def childMethod(self):
        print("Child method!")
    def childMethod1(self):
        print("Anotherd child method!")
        
derived = Child()
derived.parentMethod()
derived.parentMethod1()
derived.childMethod()
derived.childMethod1()