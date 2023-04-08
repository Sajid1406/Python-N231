# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

for row in range(1,6): 
    for col in range(5,row-1,-1): 
        print(col,end="")
    print("")

#    *
#   **
#  ***
# ****

for row in range(5):
    for col in range(4,row,-1): # Space
        print(" ",end="")
    for col in range(row):  # Star
        print("*",end="")
    print("")

# ****
# ***
# **
# *

# for row in range(4): # 1 2 3 4
#     for col in range(4,row,-1): # 4 3 2 1
#         print("*",end="")
#     print("")

          #  OR  #

for row in range(4,0,-1):
    for col in range(row):
        print("*",end="")
    print("")


#     *        
#    **
#   ***
#  ****
# *****
# ****
# ***
# **
# *

for row in range(4):
    for col in range(4,row,-1): # Space
        print(" ",end="")
    for col in range(row+1): # Star
        print("*",end="")
    print("")

for row in range(5,0,-1):
    for col in range(row):
        print("*",end="")
    print("")