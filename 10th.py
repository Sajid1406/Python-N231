##*##
#***#

# for i in range(1):
#     for j in range(2):
#         print("#",end="")
#     for k in range(1):
#         print("*",end="")
#     for j in range(2):
#         print("#",end="")
#     print("")

row = int(input("Enter a digit : "))
for i in range(row):
    for j in range(row-i-1): # space
        print(" ",end="")
    for k in range(2*i+1): # odd star
        print("*",end="")
    print("")

# for i in range(row):
#     for j in range(row-1):
#         print(" ",end="")
#     print("*")
       
        #   OR   #

for i in range(row):
    for j in range(row):
        if(j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

# One line input
list_input = [ int(i) for i in input().split(" ")] 

# Description
input_input=input()
list=[]
for i in input_input:
    if(i==" "):
        continue
    else:
        list.append(int(i))
        # print(int(i))
a=list[0]
b=list[1]
print(a)
print(b)