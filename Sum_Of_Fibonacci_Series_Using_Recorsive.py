# write a program to find the sum of fibonacci series number using recorsive function
def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number-2) + fib(number-1)
num = int(input("Enter any number"))
Sum = 0
for i in range(0,num+1):
    print(fib(i),end=" ")
    Sum = Sum + fib(i)
print(Sum)