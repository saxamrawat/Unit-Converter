

#--------------importing modules-------------

import Time as t
import Length as l
import Temperature as temp

#--------------------------------------------



print("\n\n\t\tWELCOME TO THE UNIVERSAL UNIT CONVERTER\n\n")      #title                                 

print("*"*80)  #star-line

print("\n\n\t\tPlease choose from the quantities given below : ")  #print-statement



#----------------------------------------Main Menu Function-------------------------------------

def Menu():
    Menu = ["Time", "Length", "Mass", "Volume", "Thermodynamic Temperature (TEMP)", "EXIT (e)"]

    for i in Menu:
        print("\t\t",Menu.index(i)+1,".",i)

        
#-----------------------------------------------------------------------------------------------
Menu()  #function-call

quantity = input("\t\t >")  #user-input

#-----------------------------------------------------------------------------------------------

def again():                                          #if the user want to convert more values
    print("-"*80, end="\n\n") #dash-line
    Menu()
    global quantity
    quantity = input("\t\t >")


#-------------------------------------Time Function-----------------------------------------------

    
def TIME():
#if quantity.upper() == "TIME" or quantity == "1":

    #------------------------------Sub-Menu-Time--------------------------------------------------
    print('''\n\n\t\tChoose from which unit to which other unit you want to convert : ''')
    
    Time = ["Seconds {use sec}", "Minutes {use min}", "Hours {use hour}"]
    for j in Time:
        print("\t\t",Time.index(j)+1,".",j)

    #---------------------------------------------------------------------------------------------
    timefrom = input("\n\t\tFrom: ")   #User-Input---->from value
    timeto = input("\n\t\tTo: ")       #User-Input---->to value

    #----------------------------------conversion of values---------------------------------------

    if timefrom.upper() == "SEC" or timefrom == "1":
        if timeto.upper() == "MIN" or timeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Secto.minutes(realvalue)} minutes")  
        elif timeto.upper() == "HRS" or timeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Secto.hours(realvalue)} hours")

    elif timefrom.upper() == "MIN" or timefrom == "2":
        if timeto.upper() == "SEC" or timeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Minto.sec(realvalue)} seconds")
        elif timeto.upper() == "HRS" or timeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Minto.hours(realvalue)} hours")

    elif timefrom.upper() == "HOURS" or timefrom == "3":
        if timeto.upper() == "SEC" or timeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Hoursto.sec(realvalue)} seconds")
        elif timeto.upper() == "MIN" or timeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {t.Hoursto.min(realvalue)} minutes")

#---------------------------------------if again---------------------------------------------------------------------

    print("*"*80)
    Again = input("\n\nPress \'y\' or \'Y\' if you want to go back to Menu, Any input for the same menu conversion \n\t\tand \'e\' or \'E\' if you want to exit : ")

    if Again.upper()=="Y":
        again()
    elif Again.upper()=="E":
        quit()    #EXIT

#End of the time function

#-------------------------------------Length Function-----------------------------------------------


def LENGTH():
#elif quantity.upper() == "LENGTH" or quantity == "2":

    #------------------------------Sub-Menu-Time--------------------------------------------------
    
    print('''\n\n\t\tChoose from which unit to which other unit you want to convert : ''')

    Length = ["Kilometer(KM)", "Hectometer(HM)", "Decameter(DAM)", "Meter(M)", "Decimeter(DM)", "Centimeter(CM)", "Milimeter(MM)", "Micrometer(UM)", "Nanometer(NM)"]
    for k in Length:
        print("\t\t",Length.index(k)+1,".",k)

    #---------------------------------------------------------------------------------------------
    
    lengthfrom = input("\n\t\tFrom: ")  #User_input----->from value
    lengthto = input("\n\t\tTo: ")      #User-input----->to value

    #----------------------------------conversion of values---------------------------------------

    if lengthfrom.upper() == "KM" or lengthfrom == "1":
        if lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "HM" or lengthfrom == "2":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.kilo(realvalue)} km")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "DAM" or lengthfrom == "3":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.hecto(realvalue)} hm")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.nano(realvalue)} nm")

    elif lengthfrom.upper() == "M" or lengthfrom == "4":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deca(realvalue)} dam")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "DM" or lengthfrom == "5":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {Length.Decito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.meter(realvalue)} m")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "CM" or lengthfrom == "6":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deci(realvalue)} dm")
        elif lengthto.upper() == "MM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "MM" or lengthfrom == "7":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.meter(realvalue)} m")
        elif lengthto.upper() == "CM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deci(realvalue)} dm")
        elif lengthto.upper() == "MM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.centi(realvalue)} cm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.micro(realvalue)} um")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.nano(realvalue)} nm")

    elif lengthfrom.upper() == "UM" or lengthfrom == "8":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.milli(realvalue)} mm")
        elif lengthto.upper() == "NM" or lengthto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.nano(realvalue)} nm")

    elif lengthfrom.upper() == "NM" or lengthfrom == "9":
        if lengthto.upper() == "KM" or lengthto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.kilo(realvalue)} km")
        elif lengthto.upper() == "HM" or lengthto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.hecto(realvalue)} hm")
        elif lengthto.upper() == "DAM" or lengthto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deca(realvalue)} dam")
        elif lengthto.upper() == "M" or lengthto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.meter(realvalue)} m")
        elif lengthto.upper() == "DM" or lengthto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deci(realvalue)} dm")
        elif lengthto.upper() == "CM" or lengthto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.centi(realvalue)} cm")
        elif lengthto.upper() == "MM" or lengthto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.milli(realvalue)} mm")
        elif lengthto.upper() == "UM" or lengthto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.micro(realvalue)} mm")

#-------------------------------------------------if again-----------------------------------------------------------

    print("*"*80)
    Again = input("\n\nPress \'y\' or \'Y\' if you want to go back to Menu, Any input for the same menu conversion \n\t\tand \'e\' or \'E\' if you want to exit : ")

    if Again.upper()=="Y":
        again()
    elif Again.upper()=="E":
        quit()  #EXIT

#End of Length Function

#----------------------------------------------------Mass Function----------------------------------------------------

def MASS():
#elif quantity.upper() == "MASS" or quantity == "3":

    #-----------------------------------sub-Menu for Mass-------------------------------------------------------------
    print('''\n\n\t\tChoose from which unit to which other unit you want to convert : ''')

    Mass = ["Kilogram(KG)", "Hectogram(HM)", "Decagram(DAM)", "Gram(G)", "Decigram(DG)", "Centigram(CG)", "Miligram(MG)", "Microgram(UG)", "Nanogram(NG)"]

    for m in Mass:
        print("\t\t",Mass.index(m)+1,".",m)
        
    #-----------------------------------------------------------------------------------------------------------------

    massfrom = input("\n\t\tFrom: ")   #user-input---->from value
    massto = input("\n\t\tTo: ")       #user-input---->to value

    #----------------------------------conversion of values-----------------------------------------------------------
    # Reused code and module for length
    if massfrom.upper() == "KG" or massfrom == "1":
        if massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deci(realvalue)} dg")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.nano(realvalue)} ng")

    elif massfrom.upper() == "HG" or massfrom == "2":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.kilo(realvalue)} kg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deci(realvalue)} dm")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.nano(realvalue)} ng")

    elif massfrom.upper() == "DAG" or massfrom == "3":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.hecto(realvalue)} hg")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.deci(realvalue)} dg")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.nano(realvalue)} ng")

    elif massfrom.upper() == "G" or massfrom == "4":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Valu1e: {l.Meterto.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deca(realvalue)} dag")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deci(realvalue)} dg")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.nano(realvalue)} ng")

    elif massfrom.upper() == "DG" or massfrom == "5":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.meter(realvalue)} g")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.nano(realvalue)} ng")

    elif massfrom.upper() == "CG" or massfrom == "6":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deci(realvalue)} dg")
        elif massto.upper() == "MG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.nano(realvalue)} ng")

    elif massfrom.upper() == "MG" or massfrom == "7":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.meter(realvalue)} g")
        elif massto.upper() == "CG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deci(realvalue)} dg")
        elif massto.upper() == "MG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.centi(realvalue)} cg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.micro(realvalue)} ug")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.nano(realvalue)} ng")

    elif massfrom.upper() == "UG" or massfrom == "8":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deci(realvalue)} dg")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.milli(realvalue)} mg")
        elif massto.upper() == "NG" or massto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.nano(realvalue)} ng")

    elif massfrom.upper() == "NG" or massfrom == "9":
        if massto.upper() == "KG" or massto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.kilo(realvalue)} kg")
        elif massto.upper() == "HG" or massto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.hecto(realvalue)} hg")
        elif massto.upper() == "DAG" or massto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deca(realvalue)} dag")
        elif massto.upper() == "G" or massto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.meter(realvalue)} g")
        elif massto.upper() == "DG" or massto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deci(realvalue)} dg")
        elif massto.upper() == "CG" or massto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.centi(realvalue)} cg")
        elif massto.upper() == "MG" or massto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.milli(realvalue)} mg")
        elif massto.upper() == "UG" or massto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.micro(realvalue)} mg")

#------------------------------------------------------if again------------------------------------------------------

    print("*"*80)
    Again = input("\n\nPress \'y\' or \'Y\' if you want to go back to Menu, Any input for the same menu conversion \n\t\tand \'e\' or \'E\' if you want to exit : ")

    if Again.upper()=="Y":
        again()
    elif Again.upper()=="E":
        quit()  #EXIT

#End of the Mass Function

#----------------------------------------------------Volume Function-------------------------------------------------

def VOLUME():
#elif quantity.upper() == "VOLUME" or quantity == "4":

    #-----------------------------------sub-Menu for Volume----------------------------------------------------------

    
    print('''\n\n\t\tChoose from which unit to which other unit you want to convert : ''')

    Volume = ["Kilolitre(KL)", "Hectolitre(HL)", "Decalitre(DAL)", "Litre(L)", "Decilitre(DL)", "Centilitre(CL)", "Millilitre(ML)", "Microlitre(UL)", "Nanolitre(NL)"]

    for v in Volume:
        print("\t\t",Volume.index(v)+1,".",v)

    #---------------------------------------------------------------------------------------------------------------

    volumefrom = input("\n\t\tFrom: ")     #User-input---->from value
    volumeto = input("\n\t\tTo: ")         #User-input---->to value

    #----------------------------------conversion of values---------------------------------------------------------
    
    # Reused code and module for length
    if volumefrom.upper() == "KL" or volumefrom == "1":
        if volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Kiloto.nano(realvalue)} nl")

    elif volumefrom.upper() == "HL" or volumefrom == "2":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.kilo(realvalue)} kl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Hectoto.nano(realvalue)} nl")

    elif volumefrom.upper() == "DAL" or volumefrom == "3":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.hecto(realvalue)} hl")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decato.nano(realvalue)} nl")

    elif volumefrom.upper() == "L" or volumefrom == "4":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Valu1e: {l.Meterto.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deca(realvalue)} dal")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Meterto.nano(realvalue)} nl")

    elif volumefrom.upper() == "DL" or volumefrom == "5":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.meter(realvalue)} l")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Decito.nano(realvalue)} nl")

    elif volumefrom.upper() == "CL" or volumefrom == "6":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.deci(realvalue)} dl")
        elif volumeto.upper() == "ML" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Centito.nano(realvalue)} nl")

    elif volumefrom.upper() == "ML" or volumefrom == "7":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.meter(realvalue)} l")
        elif volumeto.upper() == "CL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.deci(realvalue)} dl")
        elif volumeto.upper() == "ML" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.centi(realvalue)} cl")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.micro(realvalue)} ul")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Millito.nano(realvalue)} nl")

    elif volumefrom.upper() == "UL" or volumefrom == "8":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.milli(realvalue)} ml")
        elif volumeto.upper() == "NL" or volumeto == "9":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Microto.nano(realvalue)} nl")

    elif volumefrom.upper() == "NL" or volumefrom == "9":
        if volumeto.upper() == "KL" or volumeto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.kilo(realvalue)} kl")
        elif volumeto.upper() == "HL" or volumeto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.hecto(realvalue)} hl")
        elif volumeto.upper() == "DAL" or volumeto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deca(realvalue)} dal")
        elif volumeto.upper() == "L" or volumeto == "4":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.meter(realvalue)} l")
        elif volumeto.upper() == "DL" or volumeto == "5":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.deci(realvalue)} dl")
        elif volumeto.upper() == "CL" or volumeto == "6":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.centi(realvalue)} cl")
        elif volumeto.upper() == "ML" or volumeto == "7":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.milli(realvalue)} ml")
        elif volumeto.upper() == "UL" or volumeto == "8":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(f"\t\tConverted Value: {l.Nanoto.micro(realvalue)} ml")

#--------------------------------------------------if again----------------------------------------------------------

    print("*"*80)
    Again = input("\n\nPress \'y\' or \'Y\' if you want to go back to Menu, Any input for the same menu conversion \n\t\tand \'e\' or \'E\' if you want to exit : ")

    if Again.upper()=="Y":
        again()
    elif Again.upper()=="E":
        quit()  #EXIT

#End of the Volume function

#----------------------------------------------------Temp Function--------------------------------------------

def TEMP(): #temperature
#elif quantity.upper() == "TEMP" or quantity == "5":

    #----------------------------------sub-menu for Temp------------------------------------------------------
    print('''\n\n\t\tChoose from which unit to which other unit you want to convert : ''')

    Temp = ["Celcius(C)", "Fahrenheit(F)", "Kelvin(K)"]

    for t in Temp:
        print("\t\t",Temp.index(t)+1,".",t)

    #---------------------------------------------------------------------------------------------------------

    tempfrom = input("\n\t\tFrom: ")      #User-input---->from value
    tempto = input("\n\t\tTo: ")          #User-input---->to value

    #--------------------------------------Conversion of values-----------------------------------------------

    if tempfrom.upper() == "C" or tempfrom == "1":
        if tempto.upper() == "F" or tempto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Celsiusto.fahrenheit(realvalue)}°F")
        elif tempto.upper() == "K" or tempto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Celsiusto.kelvin(realvalue)} K")

    elif tempfrom.upper() == "F" or tempfrom == "2":
        if tempto.upper() == "C" or tempto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Fahrenheitto.celsius(realvalue)}°C")
        elif tempto.upper() == "K" or tempto == "3":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Fahrenheitto.kelvin(realvalue)} K")

    elif tempfrom.upper() == "K" or tempfrom == "3":
        if tempto.upper() == "C" or tempto == "1":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Kelvinto.celsius(realvalue)}°C")
        elif tempto.upper() == "F" or tempto == "2":
            realvalue = float(input("\n\n\t\tReal Value: "))
            print(
                f"\t\tConverted Value: {temp.Kelvinto.fahrenheit(realvalue)}°F")


#-----------------------------------------------if again------------------------------------------------------------

    print("*"*80)
    Again = input("\n\nPress \'y\' or \'Y\' if you want to go back to Menu, Any input for the same menu conversion \n\t\tand \'e\' or \'E\' if you want to exit : ")

    if Again.upper()=="Y":
        again()
    elif Again.upper()=="E":
        quit()      #EXIT

#End of the Temp function

#-------------------------------------------------------------------------------------------------------------------

#                                            Drivers Code-START

#-------------------------------------------------------------------------------------------------------------------

while True:


    if quantity.upper() == "TIME" or quantity == "1":
        TIME()

#-------------------------------------------------------------------------------------------------------------------

    if quantity.upper() == "LENGTH" or quantity == "2":
        LENGTH()

#-------------------------------------------------------------------------------------------------------------------

    if quantity.upper() == "MASS" or quantity == "3":
        MASS()

#-------------------------------------------------------------------------------------------------------------------

    if quantity.upper() == "VOLUME" or quantity == "4":
        VOLUME()

#-------------------------------------------------------------------------------------------------------------------

    if quantity.upper() == "TEMP" or quantity == "5":
        TEMP()

#-------------------------------------------------------------------------------------------------------------------

    if quantity.upper() == "E" or quantity == "6":
        quit()   #EXIT

#-------------------------------------------------------------------------------------------------------------------

#                                            Drivers Code-END


