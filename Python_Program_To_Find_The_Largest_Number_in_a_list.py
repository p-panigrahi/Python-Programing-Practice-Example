# Python program to find the largest number in a list
# Method 1
# newList = []
# Number = int(input("Enter Number of items : "))
# for i in range(1,Number+1):
#     value = int(input("Emter any value : "))
#     newList.append(value)
# print(f"The Largest number is {max(newList)}")

# Method 2 using sort
# newList = []
# Number = int(input("Enter Number of items : "))
# for i in range(1,Number+1):
#     value = int(input("Emter any value : "))
#     newList.append(value)
# newList.sort()
# print(f"The Largest number is {newList[Number-1]}")

# Method 2 Using For loop
newList = []
position = 0
Number = int(input("Enter Number of items : "))
for i in range(1,Number+1):
    value = int(input("Emter any value : "))
    newList.append(value)
largestNumber = newList[0]
for j in range(Number):
    if largestNumber < newList[j]:
        largestNumber = newList[j]
        position = j

print(f"The Largest number is {largestNumber}")
print(position)