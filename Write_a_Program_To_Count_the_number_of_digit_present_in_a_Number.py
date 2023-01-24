# write a program to count the number of digits present in a string
Number = int(input("Enter any number"))
count = 0
while Number > 0:
    Number = Number // 10
    count += 1
print(count)