message = "hello world"
print(len(message))
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.upper())
print(message.lower())
print(message.count("hello"))
print(message.count("l"))
print(message.find("world"))
# if the string is not found it returns -1
print(message.find("universe"))

new_message = message.replace("world","universe")
message = message.replace("world","universe")
print(new_message)
print(message)

greeting = "Hello"
name = "Mohan"
message = greeting + name
print(message)

message = greeting +', '+ name
print(message)

message = greeting +', '+ name+'. Welcome!'
print(message)
# formatted strings

message = '{},{}. Welcome!'.format(greeting,name)
print(message)

message = f'{greeting},{name}. Welcome!'
print(message)

message = f'{greeting},{name.upper()}. Welcome!'
print(message)
print(dir(name))
print(help(str.lower))
