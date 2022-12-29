# write a program to find the factorial of a number using function
def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact
num = int(input("Enter any number"))
result = factorial(num)
print(result)