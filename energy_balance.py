"""
energy_balance.py
Energy Balance Calculator (Q = m * c * delta_T)
"""


def run():
    print('"Energy Balance Calculator"')
    print("Formula: Q = m * c * \u0394T")
    print("Enter the values of the following in SI units only.")

    choice = input("What do you want to calculate? (Q, m, c, dT): ").strip()

    if choice == "Q":
        m = float(input("Enter mass (kg): "))
        c = float(input("Enter specific heat capacity (J/kg*K): "))
        delta_T = float(input("Enter change in temperature (K): "))
        Q = m * c * delta_T
        print(f"Heat energy (J): {Q}")

    elif choice == "m":
        Q = float(input("Enter heat energy (J): "))
        c = float(input("Enter specific heat capacity (J/kg*K): "))
        delta_T = float(input("Enter change in temperature (K): "))
        m = Q / (c * delta_T)
        print(f"Mass (kg): {m}")

    elif choice == "c":
        Q = float(input("Enter heat energy (J): "))
        m = float(input("Enter mass (kg): "))
        delta_T = float(input("Enter change in temperature (K): "))
        c = Q / (m * delta_T)
        print(f"Specific heat capacity (J/kg*K): {c}")

    elif choice == "dT":
        Q = float(input("Enter heat energy (J): "))
        m = float(input("Enter mass (kg): "))
        c = float(input("Enter specific heat capacity (J/kg*K): "))
        delta_T = Q / (m * c)
        print(f"Change in temperature (K): {delta_T}")

    else:
        print("Select variables from Energy Balance equation only (Q, m, c, dT)")


if __name__ == "__main__":
    run()
