# Dictionaries are ordered collection of data items. They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
info = {'name': 'Sam', 'age': '20', 'eligible': True}
print(info.keys())
print(info['name'])
print(info.get('name'))

# Accessing Dictionary items:
# I. Accessing single values:
# print(info['Subject']) # -> KeyError: 'Subject'
# print(info.get('Subject')) # But here you will get None

# Accessing multiple values
print(info.values())

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.
print(info.keys())

for key in info.keys():
    print(f"The value corresponding to {key} is {info[key]}")
    
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to {key} is {value}")