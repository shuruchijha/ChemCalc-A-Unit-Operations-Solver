"""
ideal_gas.py
Ideal Gas Law Calculator (PV = nRT)
"""


def run():
    print('"This is an IDEAL GAS Calculator"')
    print('"Enter the values of P, V, n and T in SI units only."')

    Q = input("What do you want to calculate? (P/V/n/T): ").strip()

    if Q == "P":
        V = float(input("Enter Volume(m^3): "))
        n = float(input("Enter Moles(mol): "))
        T = float(input("Enter Temperature(K): "))
        Question = input("Do you have gas constant(R) value? Y/N ").strip().lower()
        if Question == "y":
            R = float(input("Enter R: "))
        else:
            R = 8.314
        P = (n * R * T) / V
        print(f"-> P = {P}")

    elif Q == "V":
        P = float(input("Enter Pressure(Pa): "))
        n = float(input("Enter Moles(mol): "))
        T = float(input("Enter Temperature(K): "))
        Question = input("Do you have gas constant(R) value? Y/N ").strip().lower()
        if Question == "y":
            R = float(input("Enter R: "))
        else:
            R = 8.314
        V = (n * R * T) / P
        print(f"-> V = {V}")

    elif Q == "n":
        P = float(input("Enter Pressure(Pa): "))
        V = float(input("Enter Volume(m^3): "))
        T = float(input("Enter Temperature(K): "))
        Question = input("Do you have gas constant(R) value? Y/N ").strip().lower()
        if Question == "y":
            R = float(input("Enter R: "))
        else:
            R = 8.314
        n = (P * V) / (R * T)
        print(f"-> n = {n}")

    elif Q == "T":
        P = float(input("Enter Pressure(Pa): "))
        V = float(input("Enter Volume(m^3): "))
        n = float(input("Enter Moles(mol): "))
        Question = input("Do you have gas constant(R) value? Y/N ").strip().lower()
        if Question == "y":
            R = float(input("Enter R: "))
        else:
            R = 8.314
        T = (P * V) / (n * R)
        print(f"-> T = {T}")

    else:
        print("Select variables from Ideal Gas Equation only (P,V,n,T)")


if __name__ == "__main__":
    run()
