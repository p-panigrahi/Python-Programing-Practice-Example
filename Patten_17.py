# 1  1  1  1  1
#  2  2  2  2
#   3  3  3
#    4  4
#     5
for r in range(1,6):
    for c in range(1,6):
        if c>=r:
            print(r,end=" ")
        else:
            print(" ",end=" ")
    print()