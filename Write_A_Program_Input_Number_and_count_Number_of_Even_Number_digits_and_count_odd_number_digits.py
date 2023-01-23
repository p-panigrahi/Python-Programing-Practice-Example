# write a program to input a number and find the odd number digits and even number digits
Number = int(input("Enter any positive number"))
odd_Count = 0
even_Count = 0
temp = Number
while temp > 0:
    Remender = temp % 10
    if Remender % 2 == 0:
        even_Count += 1
    else:
        odd_Count += 1
    temp = temp // 10
print(even_Count)
print(odd_Count)