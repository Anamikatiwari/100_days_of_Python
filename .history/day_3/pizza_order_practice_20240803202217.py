# congratulations, you've got a job at python pizza. your first job is to build an automatic pizza order program.

print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want to pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25


if add_pepperoni == "Y":
    if size == "S":
        bill

    