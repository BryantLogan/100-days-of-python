height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(int(weight / (height ** 2)))
bmi_as_str = str(bmi)

print("Your BMI is: " + bmi_as_str)