# Python Program to find all occurence of a character in a string
str = input("Enter any string")
char = input("Enter any char")
count = 0
for i in range(len(str)):
    if str[i] == char:
        count += 1
print(str)
print(char)
print(count)