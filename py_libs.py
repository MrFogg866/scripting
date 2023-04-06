# python librarys and modules

# extensive libraries in  - external collections of useful functions and methods

# python comes with some integrated librarys

from random import *
import math

print(random())


num_float = 23.66

# ceil rounds up
print(math.ceil(num_float))
# floor rounds down
print(math.floor(num_float))
# gives value of pi
print(math.pi)

# modules

import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)
# print todays date
print(datetime.date.today())

print(sys.path)

def operating_system_information():
    print(os.cpu_count())

operating_system_information()

# pip python package manager

# requests website information
import requests


requests_bbc = requests.get("https://www.bbc.co.uk")

# get status code 200 all good
print(requests_bbc.status_code)
# get all contect from website
print(requests_bbc.content)
