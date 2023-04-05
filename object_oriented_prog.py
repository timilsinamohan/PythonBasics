# Object Oriented Programing with Python

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Mohan','Timilsina',5000)
emp_2 = Employee('Test', 'User',6000)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
# print(emp_1)
# print(emp_2)
# print(emp_1.fullname())
# emp_1.first = "Mohan"
# emp_1.last = "Timilsina"
# emp_1.email = "timilsina.mohan@company.com"
# emp_1.pay = 5000
#
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "test.user@company.com"
# emp_2.pay = 6000
# print(emp_1.email)
# print(emp_2.email)