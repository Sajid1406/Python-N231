# **** row==0 or col==0
# *  *
# *  *
# **** row==3 or col==3

for row in range(0,4,1): #range(4) 0 1 2 3
    for col in range(0,4,1):
        if(row==0 or col==0 or row==3 or col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print("")


# Reverse L Shape:
for row in range (4):
    for col in range (4):
        if(row==0 or col==3):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

# Inverse L Shape:
for row in range (4):
    for col in range (4):
        if(row==0 or col==0):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

# Line
for row in range(4):
    print("*",end="")

# *
# **
# ***
# ****

# for row in range(4):
#     print("*"*row)
# for row in range(4):
#     for col in range(row+1):
#         print("*",end="")
#     print("")

       #   OR   #

for row in range(5): #range(4)
    for col in range(row): #range(row+1)
        print("*",end="")
    print("")


# ****
#  ***
#   **
#    *

for row in range (4):
    for col in range(row):
        print(" ",end="")
    for col in range(4-row): 
        print("*",end="")
    print("")