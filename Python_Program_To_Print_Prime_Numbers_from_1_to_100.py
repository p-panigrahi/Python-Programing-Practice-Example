# write a program to find the prime number between 1 to 100
minNumber = int(input("Enter any number"))
maxNumber = int(input("Enter any number"))
for i in range(minNumber,maxNumber+1):
    count = 0
    for j in range(1,i+1):
        if(i % j == 0):
            count = count + 1
    if count == 2:
        print(i)

