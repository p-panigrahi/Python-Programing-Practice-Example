# Python program to count even and odd number in a list
evenCount = 0
oddCount = 0
newList = []
Number = int(input("Enter Number Of Items : "))
for i in range(1,Number+1):
    value = int(input("Enter any value : "))
    newList.append(value)
for j in range(Number):
    if newList[j] % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print(newList)
print(evenCount)
print(oddCount)