# write a program to count the number of vowel in a string
newString = input("Enter a string")
vowel_Count = 0
for i in newString:
    if i in ("a","e","i","o","u","A","E","I","O","U"):
        vowel_Count += 1
print(vowel_Count)