class Employee():

    raiseamount = 1.05
    def __init__(self,name,lastname,paycheck):
        self.name = name
        self.lastname = lastname
        self.paycheck = paycheck
        Employee.numberofemployees += 1

    def fullname(self):
        return '{} {}'.format(self.name,self.lastname)
    def raisepayment(self,amount):
        self.paycheck = self.paycheck + amount



a = Employee("asd","fdg",100)
print(a.paycheck)
a.raisepayment(1000)

print(Employee.__dict__)