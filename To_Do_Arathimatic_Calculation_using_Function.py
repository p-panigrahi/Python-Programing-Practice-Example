# write a program to do arithmatic calculation using function
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2
def floordivision(num1,num2):
    return num1 // num2
def exponent(num1,num2):
    return num1 ** num2
num1 = int(input("Enter any number"))
num2 = int(input("Enter any number"))
result1 = addition(num1,num2)
result2 = subtraction(num1,num2)
result3 = multiplication(num1,num2)
result4 = division(num1,num2)
result5 = floordivision(num1,num2)
result6 = exponent(num1,num2)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6) 