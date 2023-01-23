# 5 5 5 5 5
#   5 5 5 5
#     5 5 5
#       5 5
#         5

for r in range(1,6):
    for c in range(1,6):
        if c >= r:
            print("5",end=" ")
        else:
            print(" ",end=" ")
    print()