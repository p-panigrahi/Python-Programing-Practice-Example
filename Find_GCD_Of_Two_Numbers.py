# write a program to find the GCD of two number
num1 = float(input("Enter any number"))
num2 = float(input("Enter any number"))
i = 1
while (i <= num1 and i <= num2):
    if(num1 % i == 0 and num2 % i == 0):
        value = i
    i += 1
print(f"HCF of {num1} and {num2} is {value}" )