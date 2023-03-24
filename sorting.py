li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)
print("sorted variable:\t",s_li)
li.sort()
print("original variable:\t",li)

s_li = sorted(li,reverse=True)
print("sorted variable:\t",s_li)
li.sort(reverse=True)
print("original variable:\t",li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print("sorted tuple:\t",s_tup)

di = {'name':'Corey', 'job':'programming','age':None,'os':'Mac'}
s_di = sorted(di)
# sort the keys
print('Dict\t',s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li)
print(s_li)

s_li = sorted(li,key=abs)
print(s_li)

# simple class
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee("Mohan",25, 20000)
e2 = Employee("Meera",21, 19000)
e3 = Employee("Battu",1, 500)
employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name


# s_employes = sorted(employees,key=e_sort,reverse=True)
s_employes = sorted(employees,key=attrgetter("name"))
print(s_employes)