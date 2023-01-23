    #         1
    #       2 1
    #     3 2 1
    #   4 3 2 1
    # 5 4 3 2 1
for r in range(1,6):
    for c in range(5,0,-1):
        if c<=r:
            print(c,end=" ")
        else:
            print(" ",end=" ")
    print()
