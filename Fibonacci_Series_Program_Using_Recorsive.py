# write a program to find Fibonacci series using recorsive function
def fib(number):
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return (fib(number-2) + fib(number-1))
num = int(input("Enter any number"))
for i in range(0,num):
    print(fib(i))