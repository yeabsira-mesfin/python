class Employee:
    def getdata(self):
        self.ename = input("Please enter your name: ")
        self.eno = int(input("Please enter your e no: "))
        self.basic = int(input("Please enter your basic pay: "))
        self.pay = int(input("please enter your pay: "))
        self.hra = int(input("Please enter your hra: "))
        self.ma = int(input("Please enter your ma: "))
        self.ta = int(input("Please enter your ta: "))
        self.pf = int(input("Please enter your pf: "))
        self.lic = int(input("Please enter your lic: "))
        self.itax = int(input("Please enter your itax: "))
    def putdata(self):
        self.grosspay = self.basic+self.hra+self.ma+self.ta
        self.netpay = self.grosspay - (self.pf + self.lic + self.itax)
        print(f"""
                  Your gross pay is {self.grosspay} and 
                  Your net pay is {self.netpay} """)
        
if __name__ == "__main__":
    reocrd = Employee
    record.getdata()
    record.putdata()