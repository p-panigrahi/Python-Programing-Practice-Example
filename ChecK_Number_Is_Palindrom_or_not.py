# Python program to find the number is palindrom or note
Number =input("Enter anu positive number")
reverseNumber = Number[::-1]
if reverseNumber == Number:
    print(f"{reverseNumber} this number is palindrom")
else:
    print(f"{reverseNumber} this number is not palindrom")