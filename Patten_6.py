    #          5
    #        4 5
    #      3 4 5
    #    2 3 4 5
    #  1 2 3 4 5 

for r in range(5,0,-1):
    for c in range(1,6):
        if c >= r:
            print(c,end=" ")
        else:
            print(" ",end=" ")
    print()