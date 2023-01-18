#Python program to count positive and negative numbers in a list
positiveCount = 0
naativeCount = 0
newList = []
Number = int(input("Enter Number Of Items"))
for i in range(1,Number+1):
    value = int(input("Emter any value"))
    newList.append(value)
for j in range(Number):
    if newList[j] >= 0:
        positiveCount += 1
    else:
        naativeCount += 1
print(newList)
print(positiveCount)
print(naativeCount)