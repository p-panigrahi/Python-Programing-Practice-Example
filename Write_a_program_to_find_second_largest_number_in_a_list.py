# write a program to find the second largest number in a list
newList = []
Number = int(input("Enter Number of items"))
for i in range(1,Number+1):
    value = int(input("Enter any value"))
    newList.append(value)
a = list(set(newList))
a.sort()
print(a[-2])