language = 'Java'
if language == 'Python':
    print('Language is Python')

elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

user = "Admin"
logged_in = True
if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

user = "Admin"
logged_in = False
if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

user = "Admin"
logged_in = False
if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

a = [1,2,3]
b = [1,2,3]
print(a==b)

print(id(a))
print(id(b))
print(a is b)


condition = False
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")


condition = None
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")

# 0 is evaluated as False: Zero of any numeric type
condition = 0
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")

condition = 10
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")


condition = []
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")

condition = ''
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")

condition = {}
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")