# Structure of For loop

start=1
stop=10 #i<10
step=3
for index in range(start,stop,step):
    print(index) # 2 3 5 6 8 9

# start=-1
# stop=10
# step=1
# for index in range(stop):
# print(index)

# while loop

start=1 #initial
while start<10:
    print("Before Increment:",start)
    start=start+1
    print("After Increment:",start)

#1
start=1
stop=11
step=1
for index in range (start,stop,step):
    print(start,"X",step,"=",start*step)
    step=step+1

#2
num=1
for i in range (1,11):
    print(num,"x",i,"=",i*num)

#3
num=3
i=1
for index in range(1,11):
    print(num,"x",i,"=",i*num)
    i=i+1 #i++

# Even Odd
for num in range (1,11):
    if num%2==0:
        print("Even",num)
    else:
        print("Odd",num)    

# Hello World
for index in range (10):
    print("Hello World")

# input Hello World
range_input=int(input())
for index in range(range_input):
    print("Hello World")

# input I Love You
range_input=int(input())
for index in range(1,range_input,100):
    print("I Love You")