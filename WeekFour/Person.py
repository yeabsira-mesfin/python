class Person:
    def getdata(self):
        self.name = input("Please enter your name: ")
        self.age = int(input("Please ener your age: "))
        self.salary = int(input("Please enter your salary: "))
    def putdata(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I get paid {self.salary} every month")

if __name__ == "__main__":
    obj = Person()
    obj.getdata()
    obj.putdata()
