# tweaked version from the tutorial
temperature = float(input("What's the temperature outside?: "))

if temperature == 30:
    print("It's mildly cold outside")
    print("Drink some hot chocolate")
elif temperature < 30:
    print("It's frigid outside")
    print("Drink some hot tea")
elif temperature > 30:
    print("It's warm outside")
    print("Drink some water")
