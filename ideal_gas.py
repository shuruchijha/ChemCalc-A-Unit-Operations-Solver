P=p="P"
V=v="V"
N=n="n"
T=t="T"

print('"This is an IDEAL GAS Calculator"')
print('"Enter the values of P, V, n and T in SI units only."')
Q=input("What do you want to calculate?" )

if(Q==P):
    print("Enter the values of the following: ")
    V=float(input("Enter Volume(m^3): "))
    n=float(input("Enter Moles(mol): "))
    T=float(input("Enter Temperature(K): "))
    R=r="gas constant"
    Question=input("Do you have gas constant(R) value? Y/N ")
    Y=y="yes"
    N=n="no"
    if(Question==Y):
        float(input("Enter R: "))
        P=p=(n*R*T)/V
        print(P)
    else:
        R=r=8.314
        P=p=(n*R*T)/V
        print(P)

elif(Q==V):
    P=float(input("Enter Pressure(Pa): "))
    n=float(input("Enter Moles(mol): "))
    T=float(input("Enter Temperature(K): "))
    R=r="gas constant"
    Question=input("Do you have gas constant(R) value? Y/N ")
    Y=y="yes"
    N=n="no"
    if(Question==Y):
        float(input("Enter R: "))
        V=v=(n*R*T)/P
        print(V)
    else:
        R=r=8.314
        V=v=(n*R*T)/P
        print(V)


elif(Q==n):
    P=float(input("Enter Pressure(Pa): "))
    V=float(input("Enter Volume(m^3): "))
    T=float(input("Enter Temperature(K): "))
    R=r="gas constant"
    Question=input("Do you have gas constant(R) value? Y/N")
    Y=y="yes"
    N=n="no"
    if(Question==Y):
        float(input("Enter R: "))
        n=N=(P*V)/(R*T)
        print(n)
    else:
        R=r=8.314
        n=N=(P*V)/(R*T)
        print(n)

elif(Q==T):
    P=float(input("Enter Pressure(Pa): "))
    V=float(input("Enter Volume(m^3): "))
    n=float(input("Enter Moles(mol): "))
    R=r="gas constant"
    Question=input("Do you have gas constant(R) value? Y/N ")
    Y=y="yes"
    N=n="no"
    if(Question==Y):
        float(input("Enter R: "))
        T=t=(P*V)/(n*R)
        print(T)
    else:
        R=r=8.314
        T=t=(P*V)/(n*R)
        print(T)

else:
    print("Select variables from Ideal Gas Equation only (P,V,n,T)")