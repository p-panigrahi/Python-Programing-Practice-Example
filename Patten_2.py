# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num = 1
for r in range(1,6):
    for c in range(1,r+1):
        print(num,end=" ")
        num += 1
    print()