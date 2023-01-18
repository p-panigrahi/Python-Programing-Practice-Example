# Python program to reverse string
# str1 = input("Enter any string")
# str2 = " "
# for i in str1:
#     str2 = i + str1
# print(str1)
# print(str2)

# Using function
# def reverse(str1):
#     str2 = str1[::-1]
#     return str2
# str1 = input("Enter any string")
# str3 = reverse(str1)
# print(str1)
# print(str3)

# Using recorsion
def reverse(newList):
    if len(newList) == 0:
        return newList
    else:
        return reverse(newList[1:] + newList[0])
newList = input("Enter any string")
str3 = reverse(newList)
print(str3)