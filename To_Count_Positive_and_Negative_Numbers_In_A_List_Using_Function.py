# Python program to count positive and negative numbers in a list using function
def count_positive(newList):
    positiveCount = 0
    for j in range(Number):
        if newList[j] >= 0:
            positiveCount += 1
    return positiveCount
def count_negative(newList):
    negativeCount = 0
    for j in range(Number):
        if newList[j] < 0:
            negativeCount += 1
    return negativeCount
newList = []
Number = int(input("Enter Number of Items"))
for i in range(1,Number+1):
    value = int(input("Enter any values"))
    newList.append(value)
positive_Count = count_positive(newList)
negative_Count = count_negative(newList)
print(newList)
print(positive_Count)
print(negative_Count)