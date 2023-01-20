# python program to print palindrome number from 1 to 100
maximumNumber = int(input("Enter any positive number"))
for i in range(1,maximumNumber + 1):
    temp = i
    reverse = 0
    while temp > 0:
        remder = temp % 10
        reverse = (reverse * 10) + remder
        temp = temp // 10
    if reverse == i:
        print(i)