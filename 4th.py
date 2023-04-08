# String data type
name = " Eshikhon "
numOfOne = 12.131313414
numOfTwo = 13
print(type(numOfOne))
print(numOfOne*numOfTwo)
print(type(name+name))

# List
list = ["Hello world",3.1416,'a',12] #should be in []
print(type(list))
list = list + [1,2,3,4,5]
list[0] = [1]
print(list)

# Tuple
tuple = ("Hello world",3.1416,'a',12) #should be in ()
print(type(tuple))
tuple = tuple + (1,2,3,4,5)
print(tuple)

# Set
set = {"Hello world",3.1416,'a',1,1} #should be in {}
print(type(set))
print(set)
set.add(1)
print(set)

# Integers
a = 100
print(type(a))
print(a.bit_length())

# Floats
b = 3.1416
print(type(b))

# Complex Numbers
c = 2 + 3j
print(type(c))

# Strings
d = "Hello World"
print(type(d))
print(len(d))

# Lists
e = [1,"Hello",3.14,'a',True] #should be in []
print(type(e))
print(len(e))

# Tuples
f = (1,"Hello",3.14,'a',True) #should be in ()
print(type(f))
print(len(f))

# Sets
g = {1,"Hello",3.14,'a',True} #should be in {}
print(g)
print(type(g))
print(len(g))
h = {"apple", "banana", "cherry", True, 1, 2}
print(h)
print(len(h))

# Dictionaries
i = { "name" : "Sajid","age" : 22,"city" : "Dhaka"}
print(type(i))
print(len(i))

import json

# JSON code
json_code = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON code to a Python value
python_value = json.loads(json_code)

# Print the Python value
print(python_value)