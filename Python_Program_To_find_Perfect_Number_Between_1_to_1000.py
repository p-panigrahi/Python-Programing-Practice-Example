# Write a python program to find the perfect number between  1 to 1000
MinimumNumber = int(input("Enter any positive number"))
MaximumNumber = int(input("Enter any positive number"))
for number in range(MinimumNumber,MaximumNumber):
    sum = 0
    for n in range(1,number):
        if (number % n == 0):
            sum += n
    if (sum == number):
        print(number)