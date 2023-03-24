nums = [1,2,3,4,5,6,7,8,9,10]

# easiest loop

# my_list = []
# for n in nums:
#     my_list.append(n)

# print(my_list)
# my_list = [n for n in nums]
# print(my_list)

# I want n*n
# my_list = [n*n for n in nums]
# print(my_list)
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# Using man + lambda
# my_list = map(lambda n: n*n, nums)
# print(my_list)

# I want n for each n in nums if n is even
# my_list = [n for n in nums if n%2==0]
# print(my_list)
# Using filter + lambda
# my_list = filter(lambda n: n%2==0, nums)
# print(list(my_list))
nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# # Nested for loop
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
print(list(zip(names,heros)))
# I want a dict {'name':'hero'} for each name, hero in zip(names, heros)

# my_dict = {}
# for name, hero in zip(names,heros):
#     my_dict[name]=hero
# print(my_dict)

# Lets do with the dictionary comprehension
my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)
# I don't want Peter to add in the list
my_dict = {name : hero for name, hero in zip(names,heros) if name != "Peter"}
print(my_dict)

# set comprehension
# nums = [1,1,1,1,1,2,2,2,2,2, 3,4,5,6,7,8,9,9,9,9,10]
my_list = {n for n in nums}
print(my_list)

my_gen = (n*n for n in nums)
print(my_gen)
for i in my_gen:
    print(i)