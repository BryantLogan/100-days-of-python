height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = (round(weight / (height ** 2)))
bmi_as_str = str(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi_as_str}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi_as_str}, your weight is normal")
elif bmi < 30:
    print(f"Your bmi is {bmi_as_str}, you are overweight")
elif bmi <35:
    print(f"Your bmi is {bmi_as_str}, you are obese")
else:
    print(f"Your bmi is {bmi_as_str}, you are are clinically obese")