import json
import os

# json = json.loads(open("/Users/jooky/PycharmProjects/pythonIntro/scripting/example.json").read())
# value = json['i.p']
# print(value)


# script to creat absolute path variable
script_dir = os.path.dirname(__file__)
print("the script is located at:" + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("the script path is" + script_absolute_path)

# script parse
json = json.loads(open(script_absolute_path).read())
value = json["name"]

print(value)

# loop through keys and values, print them out
value = json
for item in value.values():
    print(item)