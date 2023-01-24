# write a program to remove the duplicate elements from the list
# newList = []
# Number = int(input("Enter Number of Items"))
# for i in range(1,Number+1):
#     value = int(input("Enter any value"))
#     newList.append(value)
# removeDuplicate = set(newList)
# final_List = list(removeDuplicate)
# print(final_List)

def remove(duplicate):
    final_List = []
    for i in duplicate:
        if i not in final_List:
            final_List.append(i)
    return final_List
newList = []
Number = int(input("Enter number of items"))
for i in range(1,Number+1):
    value = int(input("Enter any value"))
    newList.append(value)
Result = remove(newList)
print(Result)
