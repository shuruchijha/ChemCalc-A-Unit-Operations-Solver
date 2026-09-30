"""
unit_convertor.py
Unit Converter for common ChemE units (Pressure, Volume, Temperature, Mass).
"""


def convert_pressure():
    print("Units: 1=Pa 2=atm 3=bar 4=psi 5=mmHg")
    value = float(input("Enter value:"))
    frm = input("From unit (1-5):")
    to = input("To unit(1-5): ")
    if frm == to:
        print("Same unit, no conversion needed.")
    elif frm == '1' and to == '2':
        converted_value = value / 101325
        print(f"{value} Pa is equal to {converted_value} atm")
    elif frm == '1' and to == '3':
        converted_value = value / 100000
        print(f"{value} Pa is equal to {converted_value} bar")
    elif frm == '1' and to == '4':
        converted_value = value * 0.000145038
        print(f"{value} Pa is equal to {converted_value} psi")
    elif frm == '1' and to == '5':
        converted_value = value * 0.00750062
        print(f"{value} Pa is equal to {converted_value} mmHg")
    elif frm == '2' and to == '1':
        converted_value = value * 101325
        print(f"{value} atm is equal to {converted_value} Pa")
    elif frm == '2' and to == '3':
        converted_value = value * 1.01325
        print(f"{value} atm is equal to {converted_value} bar")
    elif frm == '2' and to == '4':
        converted_value = value * 14.6959
        print(f"{value} atm is equal to {converted_value} psi")
    elif frm == '2' and to == '5':
        converted_value = value * 760
        print(f"{value} atm is equal to {converted_value} mmHg")
    elif frm == '3' and to == '1':
        converted_value = value * 100000
        print(f"{value} bar is equal to {converted_value} Pa")
    elif frm == '3' and to == '2':
        converted_value = value / 1.01325
        print(f"{value} bar is equal to {converted_value} atm")
    elif frm == '3' and to == '4':
        converted_value = value * 14.5038
        print(f"{value} bar is equal to {converted_value} psi")
    elif frm == '3' and to == '5':
        converted_value = value * 750.062
        print(f"{value} bar is equal to {converted_value} mmHg")
    elif frm == '4' and to == '1':
        converted_value = value * 6894.76
        print(f"{value} psi is equal to {converted_value} Pa")
    elif frm == '4' and to == '2':
        converted_value = value / 14.6959
        print(f"{value} psi is equal to {converted_value} atm")
    elif frm == '4' and to == '3':
        converted_value = value / 14.5038
        print(f"{value} psi is equal to {converted_value} bar")
    elif frm == '4' and to == '5':
        converted_value = value * 51.7149
        print(f"{value} psi is equal to {converted_value} mmHg")
    elif frm == '5' and to == '1':
        converted_value = value * 133.322
        print(f"{value} mmHg is equal to {converted_value} Pa")
    elif frm == '5' and to == '2':
        converted_value = value / 760
        print(f"{value} mmHg is equal to {converted_value} atm")
    elif frm == '5' and to == '3':
        converted_value = value / 750.062
        print(f"{value} mmHg is equal to {converted_value} bar")
    elif frm == '5' and to == '4':
        converted_value = value / 51.7149
        print(f"{value} mmHg is equal to {converted_value} psi")
    else:
        print("Invalid unit selection.")


def convert_volume():
    print("Units: 1=m^3 2=L 3=ft^3 4=mL 5=gallon")
    value = float(input("Enter value:"))
    frm = input("From unit (1-5):")
    to = input("To unit(1-5): ")
    if frm == to:
        print("Same unit, no conversion needed.")
    elif frm == '1' and to == '2':
        converted_value = value * 1000
        print(f"{value} m^3 is equal to {converted_value} L")
    elif frm == '1' and to == '3':
        converted_value = value * 35.3147
        print(f"{value} m^3 is equal to {converted_value} ft^3")
    elif frm == '1' and to == '4':
        converted_value = value * 1e+6
        print(f"{value} m^3 is equal to {converted_value} mL")
    elif frm == '1' and to == '5':
        converted_value = value * 264.172
        print(f"{value} m^3 is equal to {converted_value} gallon")
    elif frm == '2' and to == '1':
        converted_value = value / 1000
        print(f"{value} L is equal to {converted_value} m^3")
    elif frm == '2' and to == '3':
        converted_value = value * 0.0353147
        print(f"{value} L is equal to {converted_value} ft^3")
    elif frm == '2' and to == '4':
        converted_value = value * 1000
        print(f"{value} L is equal to {converted_value} mL")
    elif frm == '2' and to == '5':
        converted_value = value * 0.264172
        print(f"{value} L is equal to {converted_value} gallon")
    elif frm == '3' and to == '1':
        converted_value = value / 35.3147
        print(f"{value} ft^3 is equal to {converted_value} m^3")
    elif frm == '3' and to == '2':
        converted_value = value / 0.0353147
        print(f"{value} ft^3 is equal to {converted_value} L")
    elif frm == '3' and to == '4':
        converted_value = value * 28316.8
        print(f"{value} ft^3 is equal to {converted_value} mL")
    elif frm == '3' and to == '5':
        converted_value = value * 7.48052
        print(f"{value} ft^3 is equal to {converted_value} gallon")
    elif frm == '4' and to == '1':
        converted_value = value / 1e+6
        print(f"{value} mL is equal to {converted_value} m^3")
    elif frm == '4' and to == '2':
        converted_value = value / 1000
        print(f"{value} mL is equal to {converted_value} L")
    elif frm == '4' and to == '3':
        converted_value = value / 28316.8
        print(f"{value} mL is equal to {converted_value} ft^3")
    elif frm == '4' and to == '5':
        converted_value = value / 3785.41
        print(f"{value} mL is equal to {converted_value} gallon")
    elif frm == '5' and to == '1':
        converted_value = value / 264.172
        print(f"{value} gallon is equal to {converted_value} m^3")
    elif frm == '5' and to == '2':
        converted_value = value / 0.264172
        print(f"{value} gallon is equal to {converted_value} L")
    elif frm == '5' and to == '3':
        converted_value = value / 7.48052
        print(f"{value} gallon is equal to {converted_value} ft^3")
    elif frm == '5' and to == '4':
        converted_value = value * 3785.41
        print(f"{value} gallon is equal to {converted_value} mL")
    else:
        print("Invalid unit selection.")


def convert_temperature():
    print("Units: 1=Kelvin(K) 2=Celsius(\u00b0C) 3=Farenheit(\u00b0F)")
    value = float(input("Enter value:"))
    frm = input("From unit (1-3):")
    to = input("To unit(1-3): ")
    if frm == to:
        print("Same unit, no conversion needed.")
    elif frm == '1' and to == '2':
        converted_value = value - 273.15
        print(f"{value} K is equal to {converted_value} \u00b0C")
    elif frm == '1' and to == '3':
        converted_value = (value - 273.15) * 9 / 5 + 32
        print(f"{value} K is equal to {converted_value} \u00b0F")
    elif frm == '2' and to == '1':
        converted_value = value + 273.15
        print(f"{value} \u00b0C is equal to {converted_value} K")
    elif frm == '2' and to == '3':
        converted_value = (value * 9 / 5) + 32
        print(f"{value} \u00b0C is equal to {converted_value} \u00b0F")
    elif frm == '3' and to == '1':
        converted_value = (value - 32) * 5 / 9 + 273.15
        print(f"{value} \u00b0F is equal to {converted_value} K")
    elif frm == '3' and to == '2':
        converted_value = (value - 32) * 5 / 9
        print(f"{value} \u00b0F is equal to {converted_value} \u00b0C")
    else:
        print("Invalid unit selection.")


def convert_mass():
    print("Units: 1=Kilogram(kg) 2=Gram(g) 3=Pound(lb) 4=Ton")
    value = float(input("Enter value:"))
    frm = input("From unit (1-4):")
    to = input("To unit(1-4): ")
    if frm == to:
        print("Same unit, no conversion needed.")
    elif frm == '1' and to == '2':
        converted_value = value * 1000
        print(f"{value} kg is equal to {converted_value} g")
    elif frm == '1' and to == '3':
        converted_value = value * 2.20462
        print(f"{value} kg is equal to {converted_value} lb")
    elif frm == '1' and to == '4':
        converted_value = value / 1000
        print(f"{value} kg is equal to {converted_value} Ton")
    elif frm == '2' and to == '1':
        converted_value = value / 1000
        print(f"{value} g is equal to {converted_value} kg")
    elif frm == '2' and to == '3':
        converted_value = value * 0.00220462
        print(f"{value} g is equal to {converted_value} lb")
    elif frm == '2' and to == '4':
        converted_value = value / 1e+6
        print(f"{value} g is equal to {converted_value} Ton")
    elif frm == '3' and to == '1':
        converted_value = value / 2.20462
        print(f"{value} lb is equal to {converted_value} kg")
    elif frm == '3' and to == '2':
        converted_value = value / 0.00220462
        print(f"{value} lb is equal to {converted_value} g")
    elif frm == '3' and to == '4':
        converted_value = value / 2204.62
        print(f"{value} lb is equal to {converted_value} Ton")
    elif frm == '4' and to == '1':
        converted_value = value * 1000
        print(f"{value} Ton is equal to {converted_value} kg")
    elif frm == '4' and to == '2':
        converted_value = value * 1e+6
        print(f"{value} Ton is equal to {converted_value} g")
    elif frm == '4' and to == '3':
        converted_value = value * 2204.62
        print(f"{value} Ton is equal to {converted_value} lb")
    else:
        print("Invalid unit selection.")


def run():
    print('"UNIT CONVERTOR"')
    print("Units:")
    print("1. Pressure")
    print("2. Volume")
    print("3. Temperature")
    print("4. Mass")

    choice = input("Choose unit from 1-4: ")

    if choice == '1':
        convert_pressure()
    elif choice == '2':
        convert_volume()
    elif choice == '3':
        convert_temperature()
    elif choice == '4':
        convert_mass()
    else:
        print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    run()
