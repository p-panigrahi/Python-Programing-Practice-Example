# write a program to count number of digits in a number
num = int(input("Enter positive number"))
count = 0
while (num > 0):
    num = num // 10
    count += 1
print(count)