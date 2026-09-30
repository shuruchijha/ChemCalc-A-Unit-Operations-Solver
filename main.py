"""
main.py
Menu-driven entry point for ChemCalc - Chemical Engineering Calculator.
"""

import ideal_gas
import energy_balance
import reynolds
import unit_convertor


def print_menu():
    print("\nWelcome to ChemCalc \u2697\ufe0f")
    print("================================")
    print("1. Ideal Gas Law (PV = nRT)")
    print("2. Energy Balance (Q = mCp\u0394T)")
    print("3. Reynolds Number")
    print("4. Unit Converter")
    print("0. Exit")


def main():
    while True:
        print_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            ideal_gas.run()
        elif choice == "2":
            energy_balance.run()
        elif choice == "3":
            reynolds.run()
        elif choice == "4":
            unit_convertor.run()
        elif choice == "0":
            print("Exiting ChemCalc. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
