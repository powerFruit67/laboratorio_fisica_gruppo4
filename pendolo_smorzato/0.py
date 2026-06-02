import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# grafico dei punti
tempo, tetaP = np.loadtxt("./0.csv", delimiter=",", unpack=True, skiprows=1)
teta = tetaP / 180 * np.pi
fig, ax = mp.subplots()
ax.set_xlabel("TEMPO (s)", fontsize=11)
ax.set_ylabel("TETA (rad)", fontsize=11)
ticklist = np.arange(0, 100, 10)
ticklabel = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
tempoErr = 0.1 * np.ones(len(teta))
tetaErr = (0.18 / 180 * np.pi) * np.ones(len(teta))
ax.axhline(0, c="k", lw=0.5)
ax.errorbar(
    tempo,
    teta,
    xerr=tempoErr,
    yerr=tetaErr,
    ls="-",
    lw=0.25,
    c="r",
    marker="o",
    mfc="r",
    ms=0.5,
    mec="r",
)


# calcolo linea di approssimazione
def f(tempo, teta0, gamma, omega, phi):
    return teta0 * np.exp(-gamma * tempo) * np.sin(omega * tempo + phi)


parametri, covar = optimize.curve_fit(f, tempo, teta)
print(parametri)
fig2, ax2 = mp.subplots()
ax2.set_title("corrente = 0A", fontsize=16, pad=15)
ax2.set_xlabel("TEMPO (s)", fontsize=11)
ax2.set_xlim(left=0)
ax2.set_ylabel("TETA (rad)", fontsize=11)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.xaxis.set_minor_locator(MultipleLocator(1.25))
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.axhline(0, c="k", lw=0.5)
ax2.errorbar(
    tempo,
    teta,
    ls="none",
    marker="o",
    ms=2,
    mfc="r",
    mec="r",
    label="valori sperimentali",
)
tempo2 = np.arange(0.8, 84.1, 0.1)
ax2.errorbar(
    tempo2, f(tempo2, *parametri), ls="-", lw=1, c="k", label="curva di approssimazione"
)
val1 = round(parametri[0], 2)
val2 = round(parametri[1], 2)
val3 = round(parametri[2], 2)
val4 = round(parametri[3], 2)
ax2.axhline(0, c="k", lw=0.5)
ax2.legend(loc="best")
ax2.text(
    50,
    1.5,
    rf"$\Theta$ = ${val1:.2f}e^{{{val2:.2f}t}}sin({val3:.2f}t {val4:+.2f})$",
    fontsize=11,
    bbox=dict(facecolor="white", edgecolor="black", lw=0.5),
)
mp.show()
