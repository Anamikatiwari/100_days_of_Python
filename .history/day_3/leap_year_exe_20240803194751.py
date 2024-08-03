# wap that works out whwther if a given year is a leap year. A normal year has 365 days, leap year have 366, with an extra day in february. The reason why we have leap years is really fascinating.

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(is a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
     