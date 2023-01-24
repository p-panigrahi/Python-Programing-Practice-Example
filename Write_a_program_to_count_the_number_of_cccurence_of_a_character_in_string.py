# write a program to find the number of occurence of a character in a string
newString = input("Enter any string")
newChar = input("Enter any character")
count = 0
for i in newString:
    if i == newChar:
        count += 1
print(count)