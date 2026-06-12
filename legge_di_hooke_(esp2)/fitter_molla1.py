import numpy as np
from scipy import optimize
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# rappresento
x, y = np.loadtxt("./molla1.csv", delimiter=";", unpack=True, skiprows=1)
m = 0.0299


# fitting
# PARTE DA CAMBIARE IN BASE ALLA FUNZIONE
def f(t, A, omega, phi, D):
    return A * np.sin(omega * t + phi) + D


#####
parametri, covarianza = optimize.curve_fit(f, x, y, (0.06, 10, 2, 0))
print("i parametri sono:")
for i in range(0, len(parametri)):
    print(f"{i+1}: {parametri[i]}")
    i += 1
k = parametri[1] ** 2 * m
print(f"costante elastica: {k}")

# show del risultato ottenuto
ticklist = [0.500, 1, 1.5, 2, 2.50]
ticklabel = ["0.500", "1.000", "1.500", "2.000", "2.500"]
ticklisty = [-0.24, -0.22, -0.20, -0.18, -0.16, -0.14, -0.12, -0.10]
ticklabely = ["-0.24", "-0.22", "-0.20", "-0.18", "-0.16", "-0.14", "-0.12", "-0.10"]
x2 = np.arange(0, 2.917, 0.01)

fig, ax = mp.subplots()
ax.set_title("andamento su y molla 1", fontsize=16)
ax.set_xlabel("TEMPO (s)", fontsize=11)
ax.set_ylabel("y (m)", fontsize=11)
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.set_yticks(ticklisty)
ax.set_yticklabels(ticklabely)
ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="y", linewidth=0.5, alpha=0.5)
ax.errorbar(x, y, ls="-", lw=1, c="g", marker="o", mfc="g", ms=2, mec="g")
ax.errorbar(x2, f(x2, *parametri), ls="-", lw=1, c="k")
mp.show()

# graficare andamento lungo x
t, x1 = np.loadtxt("./molla1x.csv", delimiter=";", unpack=True, skiprows=1)
fig2, ax2 = mp.subplots()
ax2.set_title("andamento su x", fontsize=16, pad=15)
ax2.set_xlabel("TEMPO (s)", fontsize=11)
ax2.set_ylabel("X (m)", fontsize=11)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax2.errorbar(t, x1, ls="-", lw=1, c="k", marker="o", mfc="r", ms=2.5, mec="r")
mp.show()
