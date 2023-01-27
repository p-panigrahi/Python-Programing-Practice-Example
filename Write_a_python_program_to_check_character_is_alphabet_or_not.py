# write a python program to check character is alphabet or not
chr = input("Enter a Character")
if(chr >= 'a' and chr <= 'z') or (chr >= 'A' and chr <= 'Z'):
    print("This is a alphabet")
else:
    print("This is no a alphabet")