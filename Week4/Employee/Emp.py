class Employee:
    def getdetails(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.emp_name = input("Enter Employee Name: ")
        self.emp_designation = input("Enter Designation: ")
        print(f"""
              Empolyee Detials
              Id: {self.emp_id}
              Name: {self.emp_name}
              Designation: {self.emp_designation}
              """)