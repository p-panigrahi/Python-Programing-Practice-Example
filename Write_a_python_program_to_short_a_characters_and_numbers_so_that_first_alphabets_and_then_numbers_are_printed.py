# write a program to short character and numbers so that first alphabet and then numbersv are printed
# input A7B1R3
# output ABR137

str = "A7B1R3"
alphabet = []
number = []
for i in str:
    if i.isalpha():
        alphabet.append(i)
    else:
        number.append(i)
final_list = sorted(alphabet) + sorted(number)
Result = " ".join(final_list)
print(Result)