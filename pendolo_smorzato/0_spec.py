import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# analisi primi dati (fino a t = 50)
tempo, tetaP = np.loadtxt(
    "./0.csv", delimiter=",", unpack=True, skiprows=1, max_rows=493
)
teta = tetaP / 180 * np.pi


def f(tempo, teta0, gamma, omega, phi):
    return teta0 * np.exp(-gamma * tempo) * np.sin(omega * tempo + phi)


ticklist = np.arange(0, 51, 10)
ticklabel = ["0", "10", "20", "30", "40", "50"]
parametri, covar = optimize.curve_fit(f, tempo, teta)
print(parametri)
fig, ax = mp.subplots()
ax.set_xlim(right=51)
ax.set_title("corrente = 0A, prima parte", fontsize=16, pad=15)
ax.set_xlabel("TEMPO (s)", fontsize=11)
ax.set_xlim(left=0)
ax.set_ylabel("TETA (rad)", fontsize=11)
ax.set_xticks(ticklist)
ax.set_xticklabels(ticklabel)
ax.xaxis.set_minor_locator(MultipleLocator(1.25))
ax.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax.axhline(0, c="k", lw=0.5)
ax.errorbar(
    tempo,
    teta,
    ls="none",
    marker="o",
    ms=2,
    mfc="r",
    mec="r",
    label="valori sperimentali",
)
tempo21 = np.arange(0.8, 50.2, 0.1)
ax.errorbar(
    tempo21,
    f(tempo21, *parametri),
    ls="-",
    lw=1,
    c="k",
    label="curva di approssimazione",
)
val1 = round(parametri[0], 2)
val2 = round(parametri[1], 2)
val3 = round(parametri[2], 2)
val4 = round(parametri[3], 2)
ax.axhline(0, c="k", lw=0.5)
ax.legend(loc="best")
ax.text(
    30,
    -2,
    rf"$\Theta$ = ${val1:.2f}e^{{{val2:.2f}t}}sin({val3:.2f}t {val4:+.2f})$",
    fontsize=11,
    bbox=dict(facecolor="white", edgecolor="black", lw=0.5),
)
mp.show()
