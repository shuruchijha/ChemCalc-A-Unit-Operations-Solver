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
ChemCalc/
├── main.py              # Menu-driven entry point
├── ideal_gas.py         # Ideal Gas Law solver
├── energy_balance.py    # Energy balance calculator
├── reynolds.py          # Reynolds number calculator
├── unit_converter.py    # Unit conversion module
└── README.md
```

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/ChemCalc.git

# Navigate into the folder
cd ChemCalc

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

--- Ideal Gas Law Solver ---
Enter P (atm) [leave blank to solve]: 
Enter V (L): 10
Enter n (mol): 2
Enter T (K): 300

→ Solving for P...
→ P = 4.924 atm
```

---

## 📐 Modules

### 1. Ideal Gas Law
```
PV = nRT    where R = 0.08206 L·atm/mol·K
```
Leave any one variable empty — the program solves for it automatically.

### 2. Energy Balance
```
Q = m × Cp × ΔT
```
Useful for heat exchanger and reactor calculations.

### 3. Reynolds Number
```
Re = ρvD / μ
Re < 2100   → Laminar Flow
Re 2100–4000 → Transitional Flow
Re > 4000   → Turbulent Flow
```

### 4. Unit Converter
Supports conversions for pressure, temperature, mass, and volume.

---

## 🗺️ Roadmap

- [x] Ideal Gas Law solver
- [x] Energy Balance calculator
- [x] Reynolds Number calculator
- [x] Unit Converter
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
