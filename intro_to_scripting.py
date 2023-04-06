# python scripting

# easy to understand
# many library's
# large community
# language interoperability (python can talk to other languages easily)

# why do we care about scripting?

# automate repetitive manual tasks using code
# some examples of things to write scripts for as devops engineers

# python to query a database
# write a python script to execute a shell command
# python to create a backup
# python script to fetch I.P address of a
# python script to check the expiry date of a SSL certificate

# sys
# os
# subproces
# math
# random
# datetime
# json


# sys module
# show version of python
# import sys
# print(sys.version)
#
# # os module
# import os
# print(os.getcwd())
#
# # go to the directory you want to go
# # os.chdir("enter filepath in here )
# # print(os.chdir())
#
# # use to make new folders in the directory you are in
# os.mkdir("testing")

# subprocess module
import subprocess

# be carefull not to make a infinite loop. automate only after your happy with the manual process
subprocess.run(["python", "hello_world.py"])

# math module

import math

pi = math.pi
pi_string = str(pi)
print("the value of pi os " + pi_string)

# random module
# this creates  a random number programme
import random
random = random.randrange(1, 10)
print(random)

# datetime module
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module
import json

x = {
    "name": "john",
    "age": 30,
    "city": "london"
}

y = json.dumps(x)

print(type(y))
print(type(x))

