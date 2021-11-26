import Time
import Length

print('''Welcome to The Universal Unit Converter.

*************************************************

Please choose from the quantities given below:
1. Time
2. Length
3. Mass
4. Volume
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
1. Kilometer(KM)
2. Hectometer(HM)
3. Decameter(DAM)
4. Meter(M)
5. Decimeter(DM)
6. Centimeter(CM)
7. Milimeter(MM)
8. Micrometer(UM)
9. Nanometer(NM)''')
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
            print(f"Converted Value: {Length.Kiloto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "HM" or lengthfrom == "2":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.kilo(realvalue)} km")
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
            print(f"Converted Value: {Length.Hectoto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "DAM" or lengthfrom == "3":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.hecto(realvalue)} hm")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.nano(realvalue)} nm")

    elif lengthfrom.upper() == "M" or lengthfrom == "4":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deca(realvalue)} dam")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "DM" or lengthfrom == "5":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.meter(realvalue)} m")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "CM" or lengthfrom == "6":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deci(realvalue)} dm")
        elif lengthto.upper() == "MM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "MM" or lengthfrom == "7":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.meter(realvalue)} m")
        elif lengthto.upper() == "CM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deci(realvalue)} dm")
        elif lengthto.upper() == "MM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.centi(realvalue)} cm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "UM" or lengthfrom == "8":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.milli(realvalue)} mm")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "NM" or lengthfrom == "9":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.micro(realvalue)} mm")

elif quantity.upper() == "MASS" or quantity.upper() == "3":
    print('''Choose from which unit to which other unit you have to convert:
1. Kilogram(KG)
2. Hectogram(HM)
3. Decagram(DAM)
4. Gram(G)
5. Decigram(DG)
6. Centigram(CG)
7. Miligram(MG)
8. Microgram(UG)
9. Nanogram(NG)''')
    lengthfrom = input("From: ")
    lengthto = input("To: ")

    if lengthfrom.upper() == "KG" or lengthfrom == "1":
        if lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deci(realvalue)} dg")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.nano(realvalue)} ng")

    elif lengthfrom.upper() == "HG" or lengthfrom == "2":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.kilo(realvalue)} kg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deci(realvalue)} dm")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.nano(realvalue)} ng")

    elif lengthfrom.upper() == "DAG" or lengthfrom == "3":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.hecto(realvalue)} hg")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.deci(realvalue)} dg")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.nano(realvalue)} ng")

    elif lengthfrom.upper() == "G" or lengthfrom == "4":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Valu1e: {Length.Meterto.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deca(realvalue)} dag")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deci(realvalue)} dg")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.nano(realvalue)} ng")

    elif lengthfrom.upper() == "DG" or lengthfrom == "5":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.meter(realvalue)} g")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.nano(realvalue)} ng")

    elif lengthfrom.upper() == "CG" or lengthfrom == "6":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deci(realvalue)} dg")
        elif lengthto.upper() == "MG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.nano(realvalue)} ng")

    elif lengthfrom.upper() == "MG" or lengthfrom == "7":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.meter(realvalue)} g")
        elif lengthto.upper() == "CG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deci(realvalue)} dg")
        elif lengthto.upper() == "MG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.centi(realvalue)} cg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.micro(realvalue)} ug")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.nano(realvalue)} ng")

    elif lengthfrom.upper() == "UG" or lengthfrom == "8":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deci(realvalue)} dg")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.milli(realvalue)} mg")
        elif lengthto.upper() == "NG" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.nano(realvalue)} ng")

    elif lengthfrom.upper() == "NG" or lengthfrom == "9":
        if lengthto.upper() == "KG" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.kilo(realvalue)} kg")
        elif lengthto.upper() == "HG" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.hecto(realvalue)} hg")
        elif lengthto.upper() == "DAG" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deca(realvalue)} dag")
        elif lengthto.upper() == "G" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.meter(realvalue)} g")
        elif lengthto.upper() == "DG" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deci(realvalue)} dg")
        elif lengthto.upper() == "CG" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.centi(realvalue)} cg")
        elif lengthto.upper() == "MG" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.milli(realvalue)} mg")
        elif lengthto.upper() == "UG" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.micro(realvalue)} mg")

elif quantity.upper() == "VOLUME" or quantity.upper() == "4":
    print('''Choose from which unit to which other unit you have to convert:
    1. Kilolitre(KL)
    2. Hectolitre(HL)
    3. Decalitre(DAL)
    4. Litre(L)
    5. Decilitre(DL)
    6. Centilitre(CL)
    7. Millilitre(ML)
    8. Microlitre(UL)
    9. Nanolitre(NL)''')
    lengthfrom = input("From: ")
    lengthto = input("To: ")

    if lengthfrom.upper() == "KL" or lengthfrom == "1":
        if lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Kiloto.nano(realvalue)} nl")

    elif lengthfrom.upper() == "HL" or lengthfrom == "2":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.kilo(realvalue)} kl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Hectoto.nano(realvalue)} nl")

    elif lengthfrom.upper() == "DAL" or lengthfrom == "3":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.hecto(realvalue)} hl")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decato.nano(realvalue)} nl")

    elif lengthfrom.upper() == "L" or lengthfrom == "4":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Valu1e: {Length.Meterto.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deca(realvalue)} dal")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Meterto.nano(realvalue)} nl")

    elif lengthfrom.upper() == "DL" or lengthfrom == "5":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.meter(realvalue)} l")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Decito.nano(realvalue)} nl")

    elif lengthfrom.upper() == "CL" or lengthfrom == "6":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.deci(realvalue)} dl")
        elif lengthto.upper() == "ML" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Centito.nano(realvalue)} nl")

    elif lengthfrom.upper() == "ML" or lengthfrom == "7":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.meter(realvalue)} l")
        elif lengthto.upper() == "CL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.deci(realvalue)} dl")
        elif lengthto.upper() == "ML" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.centi(realvalue)} cl")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.micro(realvalue)} ul")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Millito.nano(realvalue)} nl")

    elif lengthfrom.upper() == "UL" or lengthfrom == "8":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.milli(realvalue)} ml")
        elif lengthto.upper() == "NL" or lengthto == "9":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Microto.nano(realvalue)} nl")

    elif lengthfrom.upper() == "NL" or lengthfrom == "9":
        if lengthto.upper() == "KL" or lengthto == "1":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.kilo(realvalue)} kl")
        elif lengthto.upper() == "HL" or lengthto == "2":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.hecto(realvalue)} hl")
        elif lengthto.upper() == "DAL" or lengthto == "3":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deca(realvalue)} dal")
        elif lengthto.upper() == "L" or lengthto == "4":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.meter(realvalue)} l")
        elif lengthto.upper() == "DL" or lengthto == "5":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.deci(realvalue)} dl")
        elif lengthto.upper() == "CL" or lengthto == "6":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.centi(realvalue)} cl")
        elif lengthto.upper() == "ML" or lengthto == "7":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.milli(realvalue)} ml")
        elif lengthto.upper() == "UL" or lengthto == "8":
            realvalue = float(input("Real Value: "))
            print(f"Converted Value: {Length.Nanoto.micro(realvalue)} ml")
