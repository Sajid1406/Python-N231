for i in range(4):
    print("*",end="")

print("\nHello",end=" ")
print("World")

for i in range(1,5,1):
    print("i:",i)
    for j in range(1,5,1):
        print("j:",j,end="")
    print("\nEnd of j")

# Number one Times table
j=1
temp=1
start=1
stop=11
step=1
for i in range(start,stop,step): # 1,11.1
    print(temp,"x",j,"=",(temp*j))

    if(j==10):
        print("you got j==11",j)
        stop=stop+11 #stop=11,stop=21
        print("stop",stop)
        temp=temp+1 #temp=2
        print("Temp=",temp)
        print("i=",i)
        j=1
        i=1
        print(i)
    j=j+1

# Number two Times table
# j=1
# for i in range(1,11,1):
#     print(i,"x",j,"=",(i*j))
#     j=j+1

# for i in range(1,101,1):
#     for j in range(1,11,1):
#         print(i,"x",j,"=",(i*j))

for i in range(4):
    for j in range(4):
        print("*",end="")
    print("")

# Assignemnt star box print
for i in range(4):
    for j in range(4):
        if(i==1 or i==4) and (j==3 or j==3):
            print("*",end=" ")
        elif i in [1,2,3] and j in [0,1,2]:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

# # Print one row of stars
# for i in range(3):
#     print("*",end=" ")

# # Print one column of stars
# for j in range(4):
#     print("*")

# for k in range(4):
#     print("*",end=" ")