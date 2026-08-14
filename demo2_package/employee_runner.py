from demo2_package.employee_module import Employee

Employee.company_name="Deloitte"
print(Employee.company_name)

emp1=Employee()
emp2=Employee()

emp1.emp_id="101"
emp1.emp_name="John"
emp1.emp_salary=1000

emp2.emp_id="201"
emp2.emp_name="Paul"
emp2.emp_salary=2000

print(emp1.emp_id, emp1.emp_name, emp1.emp_salary)

print(emp2.emp_id, emp2.emp_name, emp2.emp_salary)

print(type(emp1))

emp1.display_employee_detail()
emp2.display_employee_detail()

res=Employee.display_company_name()
print(res)


