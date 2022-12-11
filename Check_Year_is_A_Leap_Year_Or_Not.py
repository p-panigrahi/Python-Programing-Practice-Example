# write a program to check the given year is leap or not
year = int(input("Enter Any Year"))
if((year%400 == 0)or(year%4==0) and (year%100 != 0)):
    print(f"{year} this is a leap year")
else:
    print(f"{year} this is not a leap year")