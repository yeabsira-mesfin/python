class Salgrade:
    def getsal(self):
        self.basic = float(input("Enter Basic Salary: "))

        self.hra = self.basic * 0.20
        self.da = self.basic * 0.10
        self.total_salary = self.basic + self.hra + self.da

        print(f"""
              Salary Details
              Basic Salary: {self.basic}
              HRA: {self.hra}
              DA: {self.da}
              Total Salary: {self.total_salary}
              """)
