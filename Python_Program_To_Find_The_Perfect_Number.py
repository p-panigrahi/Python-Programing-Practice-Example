# Write a python program to find the perfect number
Number = int(input("Enter anu positive number"))
sum = 0
for i in range(1,Number):
    if(Number % i == 0):
        sum = sum + i
if(sum == Number):
    print(f"{Number} This Number is perfect number")
else:
    print(f"{Number} This Number is not perfect number")