# write a program to check sum of fibonacci series
num = int(input("Enter any number"))
sum = 0
first_value = 0
second_value = 1
for i in range(0,num):
    print(first_value,end=" ")
    sum = sum + first_value
    Next = first_value + second_value
    first_value = second_value
    second_value = Next
print(f'The sum of fibonacci series{sum}')