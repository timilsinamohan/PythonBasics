# Do not Repeat Yourself: DRY
# def hello_func(greeting, name = "You"):
#     return ('{}, {}'.format(greeting, name) )


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math",'Art']
info = {'name': 'John', 'age': 22}
# student_info('Math', 'Art', name ='John',age=22)
# print(hello_func("Hello", name = "Mohan"))
student_info(courses, info)

student_info(*courses, **info)