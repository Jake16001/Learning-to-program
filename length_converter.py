# eigth program made | by myself
unit = input("What system will we be measuring in today? Imperial or Metric? ")
if unit.upper() == "IMPERIAL":
    imperial_measurement = input("Will this be in inches (in), feet (ft), yards (yd), or miles (mi)? ")
    if imperial_measurement.upper() == "INCHES":
        inches = float(input("How many inches? "))
        inches_feet = inches / 12
        inches_yards = inches / 36
        inches_miles = inches / 63360
        print("The following are the converted measurements:")
        print(str(inches_feet) + "feet")
        print(str(inches_yards) + "yards")
        print(str(inches_miles) + "miles")
    elif imperial_measurement.upper() == "FEET":
        feet = float(input("How many feet? "))
        feet_inches = feet * 12
        feet_yards = feet / 3
        feet_miles = feet / 5280
        print("The following are the converted measurements:")
        print(str(feet_inches) + " inches")
        print(str(feet_yards) + " yards")
        print(str(feet_miles) + " miles")
    elif imperial_measurement.upper() == "YARDS":
        yards = float(input("How many yards? "))
        yards_inches = yards * 36
        yards_feet = yards * 3
        yards_miles = yards / 1760
        print("The following are the converted measurements:")
        print(str(yards_inches) + " inches")
        print(str(yards_feet) + " feet")
        print(str(yards_miles) + " miles")
    elif imperial_measurement.upper() == "MILES":
        miles = float(input("How many miles? "))
        miles_inches = miles * 63360
        miles_feet = miles * 5280
        miles_yards = miles * 1760
        print("The following are the converted measurements:")
        print(str(miles_inches) + " inches")
        print(str(miles_feet) + " feet")
        print(str(miles_yards) + " yards")
if unit.upper() == "METRIC":
    metric_measurement = input("Will this be in millimeters (mm), centimeters (cm), meters (m), or kilometers (km)? ")
    if metric_measurement.upper() == "MILLIMETERS":
        millimeters = float(input("How many millimeters? "))
        mm_cm = millimeters / 10
        mm_m = millimeters / 1000
        mm_km = millimeters / 1e+6
        print("The following are the converted measurements:")
        print(str(mm_cm) + " centimeters")
        print(str(mm_m) + " meters")
        print(str(mm_km) + " kilometers")
    if metric_measurement.upper() == "CENTIMETERS":
        centimeters = float(input("How many centimeters? "))
        cm_mm = centimeters * 10
        cm_m = centimeters / 100
        cm_km = centimeters / 100000
        print("The following are the converted measurements:")
        print(str(cm_mm) + " millimeters")
        print(str(cm_m) + " meters")
        print(str(cm_km) + " kilometers")
    if metric_measurement.upper() == "METERS":
        meters = float(input("How many meters? "))
        m_mm = meters * 1000
        m_cm = meters * 100
        m_km = meters / 1000
        print("The following are the converted measurements:")
        print(str(m_mm) + " millimeters")
        print(str(m_cm) + " centimeters")
        print(str(m_km) + " kilometers")
    if metric_measurement.upper() == "KILOMETERS":
        kilometers = float(input("How many kilometers? "))
        km_mm = kilometers * 1e+6
        km_cm = kilometers * 100000
        km_m = kilometers * 1000
        print("The following are the converted measurements:")
        print(str(km_mm) + " millimeters")
        print(str(km_cm) + " centimeters")
        print(str(km_m) + " meters")
print("""
To continue converting measurements, please rerun the program.""")
