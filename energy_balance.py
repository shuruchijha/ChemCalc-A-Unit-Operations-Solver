print('"Energy Balance Calculator"')
print("Formula: Q = m * c * ΔT")
print("Enter the values of the following in SI units only.")
Q=input("What do you want to calculate? (Q, m, c, ΔT): ")
if(Q=="Q"):
    m=float(input("Enter mass (kg): "))
    c=float(input("Enter specific heat capacity (J/kg*K): "))
    delta_T=float(input("Enter change in temperature (K): "))
    Q=m*c*delta_T
    print(f"Heat energy (J): {Q}")
elif(Q=="m"):
    Q=float(input("Enter heat energy (J): "))
    c=float(input("Enter specific heat capacity (J/kg*K): "))
    delta_T=float(input("Enter change in temperature (K): "))
    m=Q/(c*delta_T)
    print(f"Mass (kg): {m}")
elif(Q=="c"):
    Q=float(input("Enter heat energy (J): "))
    m=float(input("Enter mass (kg): "))
    delta_T=float(input("Enter change in temperature (K): "))
    c=Q/(m*delta_T)
    print(f"Specific heat capacity (J/kg*K): {c}")
elif(Q=="delta_T"):
    Q=float(input("Enter heat energy (J): "))
    m=float(input("Enter mass (kg): "))
    c=float(input("Enter specific heat capacity (J/kg*K): "))
    delta_T=Q/(m*c)
    print(f"Change in temperature (K): {delta_T}")