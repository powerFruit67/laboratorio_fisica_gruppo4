import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

corrente, gamma1 = np.loadtxt("./gamma.csv", delimiter=";", unpack=True, skiprows=1)

# grafico senza tendenza
fig, ax = mp.subplots()
ax.set_xlabel("CORRENTE (A)", fontsize=11)
ax.set_ylabel(r"GAMMA ($s^{-1}$)", fontsize=11)
ticklabel = ["0", "0.2", "0.4", "0.6", "0.8"]
yticklist = np.arange(0, 2, 0.5)
yticklabel = ["0.50", "1.00", "1.50", "2.00"]
ticklist = np.arange(0, 1, 0.2)
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.set_yticks(yticklist)
ax.set_yticklabels(yticklabel)
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="y", linewidth=0.5, alpha=0.5)
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.errorbar(corrente, gamma1, ls="none", marker="o", mfc="b", ms=5, mec="b")


def f(x, A, B, C):
    return A * x**2 + B * x + C


parametri, covar = optimize.curve_fit(f, corrente, gamma1)
print(f"A = {parametri[0]}\nB = {parametri[1]}\nC = {parametri[2]}")
# grafico con tendenza
fig2, ax2 = mp.subplots()
ax2.set_title(r"relazione I - $\gamma$", fontsize=16, pad=15)
ax2.set_xlabel("CORRENTE (A)", fontsize=11)
ax2.set_ylabel(r"GAMMA ($s^{-1}$)", fontsize=11)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.set_yticks(yticklist)
ax2.set_yticklabels(yticklabel)
ax2.yaxis.set_minor_locator(MultipleLocator(0.25))
ax2.xaxis.set_minor_locator(MultipleLocator(0.1))
ax2.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="y", linewidth=0.5, alpha=0.5)
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax2.errorbar(
    corrente,
    gamma1,
    ls="none",
    marker="o",
    mfc="r",
    ms=3,
    mec="r",
    label="dati sperimentali",
)
corrente2 = np.arange(0, 1.01, 0.05)
ax2.errorbar(
    corrente2,
    f(corrente2, *parametri),
    ls="-",
    lw="1",
    c="b",
    marker="none",
    label="curva di approssimazione",
)
A1 = round(parametri[0], 2)
B1 = round(parametri[1], 2)
C1 = round(parametri[2], 3)
ax2.legend(loc="best")
ax2.text(
    0.1,
    1,
    rf"$\gamma$ = ${A1:.2f}x^2 {B1:+.2f}x {C1:+.2f}$",
    fontsize=11,
    bbox=dict(facecolor="white", edgecolor="black", lw=0.5),
)
mp.show()
w0 = input("inserisci w0 smorzamento critico: ")
C12 = C1 - float(w0)
coefficienti = [A1, B1, C12]
radici = np.roots(coefficienti)
for n in radici:
    if n >= 0:
        print(f"I = {n}")
