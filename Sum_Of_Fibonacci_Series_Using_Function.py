# write a program to find the sum of fibonacci series using function
def fib(number):
    First = 0
    Second = 1
    Sum = 0
    for i in range(0,number):
        print(First,end = " ")
        Sum = Sum + First
        Next = First + Second
        First = Second
        Second = Next
    return Sum
num = int(input("Enter any number"))
result = fib(num)
print(result)