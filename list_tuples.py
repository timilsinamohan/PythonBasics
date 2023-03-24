courses = ['History', 'Maths','Physiscs','CompSci']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[3])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])
#
# # negative index
# print(courses[-1])
# print(courses[-2])
#
# # adding items
# courses.append("Art")
# print(courses)
# courses.insert(0,"Art")
# print(courses)
courses_2 = ['Art', 'Education']
# courses.insert(0,courses_2)
# print(courses)
# print(courses[0])

courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

courses.remove('Maths')
print(courses)

# removing as a stack or queue
popped = courses.pop()
print(popped)
print(courses)

# sort and reverse
courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1,5,2,4,3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)
sorted_course = sorted(courses)
print(courses)
print(sorted_course)


print(min(nums))
print(max(nums))
print(sum(nums))


#again for the string
courses = ['History', 'Maths','Physiscs','CompSci']
print(courses.index('CompSci'))

print('Art' in courses)
print('Maths' in courses)

for item in courses:
    print(item)

for index,item in enumerate(courses):
    print(index,item)
print("****************")
for index,item in enumerate(courses, start = 1):
    print(index,item)

print("****************")
courses = ['History', 'Maths','Physiscs','CompSci']
courses_str = ','.join(courses)
print(courses_str)

courses_str = '-'.join(courses)
print(courses_str)

new_list = courses_str.split('-')
print(new_list)

print("Tuples and List")
print("Mutable")
list_1 = ['History', 'Maths','Physiscs','CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)


print("Tuples")
print("Immutable")
tuple_1 = ('History', 'Maths','Physiscs','CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

print("Sets")
cs_course = {'History', 'Maths','Physiscs','CompSci','Maths'}
art_course = {'History', 'Maths','Art','Design'}
print(cs_course)
print('Maths' in cs_course)

print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))