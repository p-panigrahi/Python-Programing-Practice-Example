# Python program to check a number is prime or note
Number = int(input("Enter any number"))
count = 0
for i in range(1,Number+1):
    if Number % i == 0:
        count += 1
if count == 2:
    print(f"{Number} is prime")
else:
    print(f"{Number} is not prime")

