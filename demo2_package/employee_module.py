class Employee:
    #static variable
    company_name=None

# constructor
    def __init__(self):
        #Non static variable
        self.emp_id=None
        self.emp_name=None
        self.emp_salary=None


    def display_employee_detail(self):
        print("Employee Id", self.emp_id)
        print("Employee Name", self.emp_name)
        print("Salary", self.emp_salary)
        print("CompanyName", Employee.company_name)
        print("***********************************************************************")

    @staticmethod
    def display_company_name():
        return Employee.company_name





