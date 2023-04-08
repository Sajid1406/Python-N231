# def hello():
#     print("Hello")       
# a=hello()
# print(a)

# def sum(a,b):
#     return a+b
# one = int(input())
# two = int(input())
# resultOne=sum(one,two)
# resultTwo=sum(11,100)
# print(resultOne)
# print(resultTwo)

# Dictionary
def show(**args):
    print(args)
show(name="Hi",age=21,school="BUBT",PI=3.1416)

# Tuples
def view(*args):
    print(args)
view("Hi",21,"BUBT",3.1416)

# Recursion 1-10
def show(num):
    print(num)
    if num==10:
        return
    show(num+1)
show(1)

# Global Variable vs Local
x = 10 # Global
x ="3.1456"

def my_func():
    x=3 # Local
    print("In the function:",x)
my_func()
print("Global Varibale:",x)

# def view():
#     x=10
#     print(x)

# view()
# x=11
# print(x)