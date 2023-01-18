# python program to remove punctuation in a string
punctuation = ''' `~!@#$%^&*()-_=+{}[]\/;:'".<>?'''
orgString = "Hello!!!, Welcome, Tutorial -_ Python"
newString = " "
for i in orgString:
    if i not in punctuation:
        newString += i
print(punctuation)
print(orgString)
print(newString)