# ⚗️ ChemCalc — Chemical Engineering Calculator

A command-line toolkit that solves common Chemical Engineering problems. Built by a ChemE student to bridge the gap between engineering fundamentals and programming.

---

## 🚀 Features

- **Ideal Gas Law** — Solve for P, V, n, or T given any three variables
- **Energy Balance** — Calculate heat duty using Q = mCpΔT
- **Reynolds Number** — Determine laminar or turbulent flow
- **Unit Converter** — Convert between common ChemE units (Pa↔atm, °C↔K, kg↔lb, etc.)

---

## 🛠️ Tech Stack

- Python 3.x
- No external libraries required (pure Python)

---

## 📁 Project Structure

```
ChemCalc-A-Unit-Operations-Solver/
├── main.py              # Menu-driven entry point
├── ideal_gas.py         # Ideal Gas Law solver
├── energy_balance.py    # Energy balance calculator
├── reynolds.py          # Reynolds number calculator
├── unit_convertor.py    # Unit conversion module
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/shuruchijha/ChemCalc-A-Unit-Operations-Solver.git

# Navigate into the folder
cd ChemCalc-A-Unit-Operations-Solver

# Run the app
python main.py
```

---

## 💡 Usage Example

```
Welcome to ChemCalc ⚗️
================================
1. Ideal Gas Law (PV = nRT)
2. Energy Balance (Q = mCpΔT)
3. Reynolds Number
4. Unit Converter
0. Exit

Enter choice: 1

"This is an IDEAL GAS Calculator"
"Enter the values of P, V, n and T in SI units only."
What do you want to calculate? (P/V/n/T): P
Enter Volume(m^3): 10
Enter Moles(mol): 2
Enter Temperature(K): 300
Do you have gas constant(R) value? Y/N N
-> P = 498.84
```

---

## 📐 Modules

### 1. Ideal Gas Law
```
PV = nRT    where R = 8.314 J/mol·K (default, or your own value)
```
Choose which variable (P, V, n or T) to solve for — the other three are taken as inputs.

### 2. Energy Balance
```
Q = m × c × ΔT
```
Useful for heat exchanger and reactor calculations.

### 3. Reynolds Number
```
Re = ρvD / μ
Re < 2100    → Laminar Flow
2100–4000    → Transitional Flow
Re > 4000    → Turbulent Flow
```

### 4. Unit Converter
Supports conversions for pressure, volume, temperature, and mass.

---

## 🗺️ Roadmap

- [x] Ideal Gas Law solver
- [x] Energy Balance calculator
- [x] Reynolds Number calculator
- [x] Unit Convertor
- [ ] Raoult's Law / VLE calculator
- [ ] LMTD (Heat Exchanger) solver
- [ ] Matplotlib graphs for VLE curves
- [ ] Streamlit web app version

---

## 👩‍💻 About

Built as a first Python project by a Chemical Engineering student (2nd year, graduating 2029).
The goal: combine ChemE domain knowledge with programming to build tools that are actually useful for engineers.

---

## 📜 License

MIT License — feel free to use and build on this!
