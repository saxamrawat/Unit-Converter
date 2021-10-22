import Time
import Length

print('''Welcome to The Universal Unit Converter.

*************************************************

Please choose from the quantities given below:
1. Time
2. Length
3. Mass
4. Electric Current
5. Thermodynamic Temperature
6. Amount Of Substance
7. Luminous Intensity''')

quantity = input("> ")

if quantity.upper() == "TIME" or quantity.upper() == "1":
    print('''Choose from which unit to which other unit you have to convert:
1. Seconds(use sec)
2. Minutes(use min)
3. Hours(use hour)''')
    timefrom = input("From: ")
    timeto = input("To: ")

    if timefrom.upper() == "SEC" or timefrom == "1":
        if timeto.upper() == "MIN" or timeto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Secto.minutes(realvalue)} minutes")
        elif timeto.upper() == "HRS" or timeto() == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Secto.hours(realvalue)} hours")

    elif timefrom.upper() == "MIN" or timefrom() == "2":
        if timeto.upper() == "SEC" or timeto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Minto.sec(realvalue)} seconds")
        elif timeto() == "HRS" or timeto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Minto.hours(realvalue)} hours")

    elif timefrom.upper() == "HOURS" or timefrom() == "3":
        if timeto.upper() == "SEC" or timeto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Hoursto.sec(realvalue)} seconds")
        elif timeto.upper() == "MIN" or timeto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Time.Hoursto.min(realvalue)} minutes")


elif quantity.upper() == "LENGTH" or quantity.upper() == "2":
    print('''Choose from which unit to which other unit you have to convert:
1. Kilometer
2. Hectometer
3. Decameter
4. Meter
5. Decimeter
6. Centimeter
7. Milimeter
8. Micrometer
9. Nanometer''')
    lengthfrom = input("From: ")
    lengthto = input("To: ")

    if lengthfrom.upper() == "KM" or lengthfrom == "1":
        if lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.mili(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "HM" or lengthfrom == "2":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.mili(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.nano(realvalue)} nm")
