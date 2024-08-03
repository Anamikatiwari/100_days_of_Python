#create a program using maths and f-string that teels us how many days, weeks, months we have left if we live until 90 years old.
age= input("What is your current age?")

age_as_int = int(age)

years_remaining =90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12