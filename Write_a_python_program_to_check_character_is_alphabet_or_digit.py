# write a program to check the character is alphabet or digit
chr = input("Enter a character")
if(chr >= 'a' and chr <= 'z') or (chr >= "A" and chr <= "Z"):
    print("This is alphabet")
elif (chr >= '0' and chr <= '9'):
    print("This is digit")
else:
    print("This is a spical character")