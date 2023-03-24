import os
from datetime import datetime
# dir will show all the attribute and methods that we can use
# print(dir(os))
# print(os.getcwd())

# list the directory


# Lets create the folder in the working directory
# os.mkdir("test_directory")
# for subdirectory
# os.makedirs("test_directory/newSubDirectory")
# print(os.listdir())
# remove dirs
# os.removedirs("test_directory/newSubDirectory")
#
# print(os.listdir())
# # size of the file
# print(os.stat("dictionaries.py").st_size)
#
# # Last modification file
# print(os.stat("dictionaries.py").st_mtime)
# mod_time = os.stat("dictionaries.py").st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirname, filenames in os.walk(os.getcwd()):
#     print("Current Path", dirpath)
#     print("Directories",dirname)
#     print("Files", filenames)
# print(os.environ.get("HOME"))
file_path = os.path.join(os.environ.get("HOME") + 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))

# split the extension of the file
print(os.path.splitext('/tmp/test.txt'))