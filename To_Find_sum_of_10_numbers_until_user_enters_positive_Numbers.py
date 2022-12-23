# write a program to find sum of 10 numbers until user enters positive numbers
sum = 0
for i in range(1,11):
    num = int(input("Enter any number"))
    if num < 0:
        break
    sum += num
print(f"The sum of positive number {sum}")