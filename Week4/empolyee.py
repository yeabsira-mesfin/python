from department import *
class Employee(Department):
    def setTemp(self, no,name):
        self.eno = no
        self.ename = name
    def putTemp(self):
        print(f""" Employee number = {self.eno} and employee name = {self.ename} """)