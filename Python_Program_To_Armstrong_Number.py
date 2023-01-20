# write a program to find the aramstrong number
Number = int(input("Enter any number "))
temp = Number 
Length = 0
sum = 0
while temp > 0:
    temp = temp // 10
    Length += 1  
temp = Number 
while temp > 0:
        remder = temp % 10
        sum = sum+(remder ** Length)
        temp = temp // 10
if sum == Number:
        print(f"{Number} This number is aramstrong number")
else:
        print(f"{Number} This number is not aramstrong number")