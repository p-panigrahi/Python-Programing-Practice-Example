# 5 5 5 5 5
#   4 4 4 4
#     3 3 3
#       2 2
#         1
#         1
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5
for r in range(5,0,-1):
    for c in range(5,0,-1):
        if c <= r:
            print(r,end=" ")
        else:
            print(" ",end=" ")
    print()
for r in range(1,6):
    for c in range(5,0,-1):
        if c <= r:
            print(r,end=" ")
        else:
            print(" ",end=" ")
    print()