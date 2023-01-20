# write a program to find the first digits of a number
Number = int(input("Enter any positive number"))
first_digits = Number
while first_digits >= 10:
    first_digits = first_digits // 10
print(first_digits)