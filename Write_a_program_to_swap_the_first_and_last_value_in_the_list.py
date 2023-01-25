# write a program to swap the first and last value in a list
newList = []
Number = int(input("Enter Number of items"))
for i in range(1,Number+1):
    value = int(input("Enter any value"))
    newList.append(value)
print(newList)
index1 = int(input("Enter First Index value"))
index2 = int(input("Enter Second Index value"))
newList[index1],newList[index2] = newList[index2],newList[index1]
print(newList)