# write a program to find the first digits of a number
num = int(input("Enter any number"))
first_digits = num
while first_digits >= 10:
    first_digits = first_digits // 10
print(first_digits)