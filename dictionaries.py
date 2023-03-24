student = {"name":"John", "age":25, "courses":['Math','CompSci']}
# print(student)
# print(student["name"])
# print(student["courses"])
# print(student.get('name'))
# print(student.get('phone'))
# print(student.get('phone',"Not Found"))
# student["phone"]='555-5555'
# # Update student name to Jane
# student["name"]='Jane'
# # print(student.get('phone',"Not Found"))
# print(student)

# Update the student dictionary

# student.update({'name':'Jane','age':35,'phone':'555-5555'})
# print(student)

# del student['age']
# print(student)

# age = student.pop('age')
# print(student)
# print(age)
#
#Looping keys and values
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,value)

