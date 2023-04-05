# Object Oriented Programing with Python

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Mohan','Timilsina',5000)
emp_2 = Employee('Test', 'User',6000)
import datetime
my_date = datetime.date(2023,4,8)
print(my_date)
print(Employee.is_workday(my_date))


emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-9000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)