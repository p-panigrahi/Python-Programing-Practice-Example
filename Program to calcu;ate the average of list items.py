# Python program to find the average of list items
newList = []
Number = int(input("Enter Number Of Items"))
for i in range(1,Number+1):
    value = int(input("Enter any value"))
    newList.append(value)
total = sum(newList)
avg = total/Number
print(newList)
print(total)
print(avg)