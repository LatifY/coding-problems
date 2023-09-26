'''WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG WRONG 
class Employee:
    def __init__(self,fullname,salary,height,nationality,**kwargs):
        self.fullname = fullname
        self.firstname, self.lastname = self.fullname.split()
        self.salary = salary
        self.height = height
        self.nationality = nationality
        self.subordinates = subordinates
'''
#answer
class Employee:
    def __init__(self,fullname,**kwargs):
        self.fullname = fullname
        self.firstname, self.lastname = self.fullname.split()
        self.salary = kwargs.get('salary',None)
        self.height = kwargs.get('height',None)
        self.nationality = kwargs.get('nationality',None)
        self.subordinates = kwargs.get('subordinates',None)
#answer

#answer alternative
class Employee2:
    
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name, self.lastname = full_name.split()
        self.__dict__.update(kwargs)
#answer alternative


#inputs
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")


print(mary.salary)
