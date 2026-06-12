import numpy as np
from scipy import optimize
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# rappresento
x, y = np.loadtxt("./molla2.csv", delimiter=";", unpack=True, skiprows=1)
m = 0.0299


# fitting
# PARTE DA CAMBIARE IN BASE ALLA FUNZIONE
def f(t, A, omega, phi, D):
    return A * np.sin(omega * t + phi) + D


#####
parametri, covarianza = optimize.curve_fit(f, x, y, (0.017, 14, 0, 0))
print("i parametri sono:")
for i in range(0, len(parametri)):
    print(f"{i+1}: {parametri[i]}")
    i += 1
k = parametri[1] ** 2 * m
print(f"costante elastica: {k}")

# show del risultato ottenuto
ticklist = [0.250, 0.500, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25]
ticklabel = [
    "0.250",
    "0.500",
    "0.750",
    "1.000",
    "1.250",
    "1.500",
    "1.750",
    "2.000",
    "2.250",
]
ticklisty = [-0.035, -0.030, -0.025, -0.020, -0.015, -0.010, -0.005, 0]
ticklabely = ["-0.035", "-0.030", "-0.025", "-0.020", "-0.015", "-0.010", "-0.005", "0"]
x2 = np.arange(0.001, 2.235, 0.001)
fig, ax = mp.subplots()
ax.set_title("andamento su y molla 2", fontsize=16)
ax.set_xlabel("TEMPO (s)", fontsize=11)
ax.set_ylabel("y (m)", fontsize=11)
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.xaxis.set_minor_locator(MultipleLocator(0.125))
ax.set_yticks(ticklisty)
ax.set_yticklabels(ticklabely)
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax.errorbar(x, y, ls="-", lw=1, c="g", marker="o", mfc="g", ms=2, mec="g")
ax.errorbar(x2, f(x2, *parametri), ls="-", lw=1, c="k")
mp.show()

t, x1 = np.loadtxt("./molla2x.csv", delimiter=";", unpack=True, skiprows=1)
fig2, ax2 = mp.subplots()
ax2.set_title("andamento su x", fontsize=16, pad=15)
ax2.set_xlabel("TEMPO (s)", fontsize=11)
ax2.set_ylabel("X (m)", fontsize=11)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax2.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax2.errorbar(t, x1, ls="-", lw=1, c="k", marker="o", mfc="r", ms=2.5, mec="r")
mp.show()
