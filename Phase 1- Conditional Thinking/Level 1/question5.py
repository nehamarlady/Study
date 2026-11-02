year = int(input("enter an year: "))
if( year % 4 == 0):
    if (year % 100 == 0 and year % 400 != 0):
        print("the year is not leap year")
    else:
        print("the year is leap year")
else:
    print("the year is not leap year")