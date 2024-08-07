# In the string code, you'll find the solution from the leap year challenge. First, convert this function is _leap() so that instead of printing "Leap year", or "Not leap year", it should return True if it is a leap year and return false if it is not a leap year. 
#You are then going to create a function called days_in_month() which will take a year and a month as input.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, ]
    
