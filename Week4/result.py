from mark import *
class Result(Mark):
    def calc(self):
        self.total = self.mark1 + self.mark2
    def putTotal(self):
        print(f""" Total: {self.total} """)