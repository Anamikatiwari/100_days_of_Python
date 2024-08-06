# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy. 
#number of cans = (wall height *)
test_h = int(input("Height os wall: "))
test_w = int(input("Width os wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)