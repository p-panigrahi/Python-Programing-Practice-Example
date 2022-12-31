# write a program to find the last digit in a number using function
def Last_digits(num):
    Last_digits = num % 10
    return Last_digits
num = int(input("Enter any number"))
result = Last_digits(num)
print(result)