# third program made | by myself
height = float(input("What is your height: "))
unit = input("Is this in inches (in) or centimeters (cm)?: ")

if unit.upper() == "INCHES" or unit.upper() == "IN" or unit.upper() == "I":
    converted = height * 2.54
    print("Height in centimeters (cm):" + str(converted))
elif unit.upper() == "CENTIMETERS" or unit.upper() == "CM" or unit.upper() == "C":
    converted = height / 2.54
    print("Height in inches (in):" + str(converted))
