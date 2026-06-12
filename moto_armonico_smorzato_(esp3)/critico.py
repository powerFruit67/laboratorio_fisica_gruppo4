import numpy as np
from scipy import optimize, signal
import matplotlib.pyplot as mp
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

tempo, tetaP = np.loadtxt("./1,38.csv", delimiter=",", unpack=True, skiprows=1)
teta = tetaP / 180 * np.pi


# calcolo linea di approssimazione
def f(tempo, gamma, A, B):
    return (A * tempo + B) * np.exp(-gamma * tempo)


ticklist = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
ticklabel = ["0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5"]
parametri, covar = optimize.curve_fit(f, tempo, teta, (3.43, 3, -2))
print(parametri)
fig2, ax2 = mp.subplots()
ax2.set_title("corrente = 1.38A", fontsize=16, pad=15)
ax2.set_xlabel("TEMPO (s)", fontsize=11)
ax2.set_ylabel("TETA (rad)", fontsize=11)
ax2.set_xlim(left=0.0, right=4.0)
ax2.set_xticks(ticklist)
ax2.set_xticklabels(ticklabel)
ax2.xaxis.set_minor_locator(MultipleLocator(0.25))
ax2.grid(which="major", axis="x", linewidth=1, alpha=0.7)
ax2.grid(which="minor", axis="x", linewidth=0.5, alpha=0.5)
ax2.axhline(0, c="k", lw=0.5)
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
tempo2 = np.arange(0.7, 3.9, 0.1)
ax2.errorbar(
    tempo2, f(tempo2, *parametri), ls="-", lw=1, c="b", label="curva di approssimazione"
)

val1 = round(parametri[0], 2)
val2 = round(parametri[1], 2)
val3 = round(parametri[2], 2)
ax2.axhline(0, c="k", lw=0.5)
ax2.legend(loc="lower right")
ax2.text(
    1.5,
    -1.5,
    rf"$\Theta$ = $e^{{-{val1:.2f}t}}[{val2:.2f}t {val3:+.2f}]$",
    fontsize=11,
    bbox=dict(facecolor="white", edgecolor="black", lw=0.5),
)
mp.show()
