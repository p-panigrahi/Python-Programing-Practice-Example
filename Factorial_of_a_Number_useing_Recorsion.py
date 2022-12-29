# write a program to find the factorial of number using recorsion
def factorial(number):
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)
num = int(input("Enter any number"))
result = factorial(num)
print(result)