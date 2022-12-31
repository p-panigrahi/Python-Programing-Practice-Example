# write a program to find the first dights of a number using function
def First_digits(num):
    first_digits = num
    while first_digits >= 10:
        first_digits = first_digits // 10
    return first_digits
num = int(input("Enter any number"))
result = First_digits(num)
print(result)