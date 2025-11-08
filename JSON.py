import json

# Python object to json data
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, 
          "titles": ["engineer", "programmer"]}

# Indent is used for formatting
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# Creates a file named person.json which dumps 
# the contents above which is in json format
# using write or w
# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# Convert JSON back to python object
# make sure to comment the with and dump python section 
# print("\nPython Dictionary since its a JSON to Python Object Conversion")
# person = json.loads(personJSON)
# print(person)

# Open the person.json file using read or r
# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

# Using classes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not  JSON serializable")

# Convert class to JSON format using the custom encode function
userJSON = json.dumps(user, default=encode_user)

# Shows {"name": "Max", "age": 27, "User": true}
print(userJSON)