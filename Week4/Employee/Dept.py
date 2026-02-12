class Dept:
    def getdata(self):
        self.dept_id = int(input("Enter Department ID: "))
        self.dept_name = input("Enter Department Name: ")
        self.location = input("Enter Department Location: ")

        print(f"""
              Department Details
              Department ID: {self.dept_id}
              Department Name: {self.dept_name}
              Department Location: {self.location}
              """)
