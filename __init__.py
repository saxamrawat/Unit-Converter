import Time

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

quantity = input(">")

if quantity.upper() == "TIME":
    print('''Choose from which unit to which other unit you have to convert:
    1. Seconds(use sec)
    2. Minutes(use min)
    3. Hours(use hour)''')
    timefrom = input("From: ")
    timeto = input("To: ")

    if timefrom.upper() == "SEC":
        if timeto.upper() == "MIN":
            realvalue = int(input("Real Value: "))
            print(f"Converted Value: {Time.sectomin(realvalue)} minutes")
        if timeto.upper() == "HOUR":
            realvalue = int(input("Real Value: "))
            print(f"Converted Value: {Time.sectohour(realvalue)} hours")
