print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12,or 15? "))
people = int(input("How many people to split the bill?"))
# bill_with_tip= bill * (1 + tip / 100)  # or tip/100 * bill + bill
# print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
