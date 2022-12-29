# write a program to find the sum of Even and Odd Numbers
sumEven = 0
sumOdd = 0
num = int(input("Enter any number"))
for i in range(1,num+1):
    if i % 2 == 0:
        sumEven += i
    elif i % 2 != 0:
        sumOdd += i
    else:
        print("This Not a Number That is a Spical number")
print(sumEven)
print(sumOdd)