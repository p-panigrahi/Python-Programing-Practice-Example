# write a program to make a simple calculater
print('''Enter the operation you want to perfrom 
1 = Add
2 = Subtract
3 = Multiply
4 = Divide''')
opt = int(input("Chose operation from 1,2,3,4 = "))
n1 = int(input("First Number = "))
n2 = int(input("Second Number = "))
if opt == 1:
    print(n1,'+',n2,'=',n1+n2)
elif opt == 2:
    print(n1,'-',n2, '=',n1-n2)
elif opt == 3:
    print(n1,'*',n2, '=',n1*n2)
elif opt == 4:
    print(n1,'/',n2, '=',n1/n2)
else:
    print("Invalid input")

