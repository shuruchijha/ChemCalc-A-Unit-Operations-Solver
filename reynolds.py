"""
reynolds.py
Reynolds Number Calculator for pipe flow.

Re = (rho * v * D) / mu

Re < 2100        -> Laminar Flow
2100 <= Re <= 4000 -> Transitional Flow
Re > 4000        -> Turbulent Flow
"""


def calculate_reynolds(rho, v, D, mu):
    """
    Calculate the Reynolds number.

    Parameters:
        rho (float): Fluid density (kg/m^3)
        v (float): Flow velocity (m/s)
        D (float): Pipe diameter (m)
        mu (float): Dynamic viscosity (Pa.s)

    Returns:
        float: Reynolds number (dimensionless)
    """
    return (rho * v * D) / mu


def classify_flow(re):
    """Return the flow regime as a string based on Reynolds number."""
    if re < 2100:
        return "Laminar Flow"
    elif 2100 <= re <= 4000:
        return "Transitional Flow"
    else:
        return "Turbulent Flow"


def run():
    """Command-line interface for the Reynolds number calculator."""
    print("\n--- Reynolds Number Calculator ---")
    try:
        rho = float(input("Enter fluid density, rho (kg/m^3): "))
        v = float(input("Enter flow velocity, v (m/s): "))
        D = float(input("Enter pipe diameter, D (m): "))
        mu = float(input("Enter dynamic viscosity, mu (Pa.s): "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    if mu == 0:
        print("Viscosity cannot be zero.")
        return

    re = calculate_reynolds(rho, v, D, mu)
    regime = classify_flow(re)

    print(f"\n-> Re = {re:.2f}")
    print(f"-> Flow Regime: {regime}")


if __name__ == "__main__":
    run()
