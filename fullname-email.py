class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = firstname + " " + lastname
		self.email = firstname.lower()+"."+lastname.lower()+"@company.com"
		
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_4 = Employee("Joshua", "Senoron")

print(emp_1.firstname)
print(emp_2.lastname)
print(emp_3.fullname)
print(emp_4.email)