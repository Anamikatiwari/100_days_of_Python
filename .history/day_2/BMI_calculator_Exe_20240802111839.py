#wap that calculates the body mass index(BMI) from a user's weight and height
# BMI= weight(kg)/height**2(m**2)

height = input("enter your height in m:")
weight = input("enter your weight in kg:")

bmi = int(weight) / float(height)**2
bmi_as_int