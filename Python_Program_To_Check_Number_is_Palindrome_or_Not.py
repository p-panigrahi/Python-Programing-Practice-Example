# Write a pytho program to check a number is palindrome or not
Number = int(input("Enter anu positive number"))
temp = Number
reverse = 0
while temp > 0:
    remder = temp % 10
    reverse = (reverse * 10)+remder
    temp = temp // 10
if (Number == reverse):
    print(f"{reverse} this number is palindrome")
else:
    print(f"{reverse} this number is not palindrom")