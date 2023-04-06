# # os module
#
# # basic uses
#
import os
import shutil
# # prints message to terminal without print
# os.system('echo "hello world"')
#
# # os module to manipulate directories
#
# # directory
directory = "test_dir"
#
# # path to parent dir
#
parent_dir = "/Users/jooky/PycharmProjects"
#
# #  path
#
path = os.path.join(parent_dir, directory)
#
#
# # create the dir
# os.mkdir(path)
# print("directory '% s' created" % directory)

# put a file in the new directory

filename = "testfile.txt "
filepath = os.path.join(path, filename)

with open(os.path.join(path, filename), "w") as file1:
    toFile = "content of file is written here"
    file1.write(toFile)
print("file " + filename + " created in " + directory + " folder")