# write a program to print count number of digits in a number using while loop
# num = int(input("Enter Any number"))
# count = 0
# while (num > 0):
#     num = num // 10
#     count += 1
# print(count)
Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)