# write a program to input character if input character is uppercase convert into lowecase if input character is lower case then convert into upercase
char = input("Enter any character")
if char >= "A" and char <= "Z":
    value = ord(char)
    value = value + 32
    print(chr(value))
elif char >= "a" and char <= "z":
    value = ord(char)
    value = value - 32
    print(chr(value))
else:
    print(f"{char} this is no a alphabate")