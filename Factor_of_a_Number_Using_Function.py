# write a program to find the factor of a number using function
def fact(number):
    print(f"The Factor of {number} is")
    for i in range(1,number+1):
        if number % i == 0:
            print(i)
num = int(input("Enter any number"))
result = fact(num)
print(result)