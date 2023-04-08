# Lamda Function

# def functionName (Param,P2,P3/.....)

# General Case
def sum(num):
    return num+10
result = sum(10)
print(result)

sum = lambda num: num+10
print(sum(10))


# Non Lambda Function
def square(numbers):
    list_save = []
    for eachElement in numbers:
        list_save.append(eachElement**2)
    return list_save

numbers = [1,2,3,4]

newList = square(numbers)
print(newList)

# Lambda Function (Python Feature)
nums = [7,9,3,1]
square_nums = map(lambda eachElement: eachElement**2,nums) # anonymous function
print(square_nums) # Address Print
print(list(square_nums))

# Comprehension
nums = [10,11,12,13]
square = [x**2 for x in nums] # [expression for item in list(input)]
print(square)

# Even/Odd
numbers = [11,12,13,14,15]
even_numbers = [eachElement for eachElement in numbers if eachElement%2==0] # [expression for item in list if condition]
print(even_numbers)
odd_numbers = [eachElement for eachElement in numbers if eachElement%2==1]
print(odd_numbers)

# Dictionary Comprehension
numbers = [4,3,2,1]
square = {eachElement:eachElement**2 for eachElement in numbers} # {key: value for item in list}
print(square)

words = ['cat','window','hello']
word_len = {w:len(w) for w in words} # Length Function
print(word_len)

# Set Comprehension
numbers = [2,2,4,4,3,2,1,5,6,8,9]
even_numbers = {x for x in numbers if x%2==0} # {Unique Value}
# {expression for item in list}
print(even_numbers)

words = 'abracadabra'
unique_chars = {letter for letter in words if letter=="b"} 

students = [{"name":"shara","age":25},{"name":"shakil","age":24},{"name":"sajid","age":22}]
sort_st=sorted(students,key=lambda st:st["age"])
print(sort_st)