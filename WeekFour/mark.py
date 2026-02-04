from student import *
class Mark(Student):
    def setMark(self, mark1,mark2):
        self.mark1 = mark1
        self.mark2 = mark2
    def putMark(self):
        print(f""" {self.sname}'s mark is {self.mark1} and {self.mark2}""")