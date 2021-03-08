class Employee():
    def __init__(self,first,last,salary):
        self.full_name =first.title+" "+last.title()
        self.annualSalary=salary

    def give_raise(self,addSalary=5000):
        self.annualSalary+=addSalary
    
