import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

file = input("percorso file da analizzare: ")
tensione, omega = np.loadtxt(file, delimiter=";", unpack=True, skiprows=1)

# grafico senza tendenza
fig, ax = mp.subplots()
ax.set_xlabel("TENSIONE (V)", fontsize=11)
ax.set_ylabel(r"OMEGA (rad/s)", fontsize=11)
ticklabel = ["5", "6", "7", "8", "9", "10"]
yticklist = [2.5, 3, 3.5, 4, 4.5]
yticklabel = ["2.50", "3.00", "3.50", "4.00", "4.50"]
ticklist = np.arange(5, 10.1, 1)
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.set_yticks(yticklist)
ax.set_yticklabels(yticklabel)
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="y", linewidth=0.5, alpha=0.5)
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.errorbar(tensione, omega, ls="none", marker="o", mfc="b", ms=5, mec="b")


def f(x, A, B):
    return A * x + B


parametri, covar = optimize.curve_fit(f, tensione, omega)
print(f"A = {parametri[0]}\nB = {parametri[1]}")
# grafico con tendenza
fig2, ax2 = mp.subplots()
ax2.set_title(r"relazione V - $\omega$", fontsize=16, pad=15)
ax2.set_xlabel("TENSIONE (V)", fontsize=11)
ax2.set_ylabel(r"OMEGA (rad/s)", fontsize=11)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.set_yticks(yticklist)
ax2.set_yticklabels(yticklabel)
ax2.yaxis.set_minor_locator(MultipleLocator(0.25))
ax2.xaxis.set_minor_locator(MultipleLocator(0.5))
ax2.grid(which="major", axis="y", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="y", linewidth=0.5, alpha=0.5)
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax2.errorbar(
    tensione,
    omega,
    ls="none",
    marker="o",
    mfc="r",
    ms=3,
    mec="r",
    label="dati sperimentali",
)
tensione2 = np.arange(5, 10.01, 0.01)
ax2.errorbar(
    tensione2,
    f(tensione2, *parametri),
    ls="-",
    lw="1",
    c="b",
    marker="none",
    label="curva di approssimazione",
)
A1 = round(parametri[0], 3)
B1 = round(parametri[1], 3)
ax2.legend(loc="best")
ax2.text(
    8,
    2.75,
    rf"$\omega$ = ${A1:.3f}x {B1:+.3f}$",
    fontsize=11,
    bbox=dict(facecolor="white", edgecolor="black", lw=0.5),
)
mp.show()
w0 = input("inserisci w0: ")
B12 = B1 - float(w0)
x = -B12 / A1
print(f"il valore di tensione per la risonanza è: {x:.2f}V")
