from Parent import *
class Child(Parent):
    def childMethod(self):
        super(Child,self).parentMethod()
        print("Child method!")
    def childMethod1(self):
        super(Child,self).parentMethod1()
        print("Anotherd child method!")
        
derived = Child()
derived.childMethod()
derived.childMethod1()