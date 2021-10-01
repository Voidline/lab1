import matplotlib.pyplot as plt
import numpy as np


def function4():
    a = float(input(f"Амплитуда "))
    t = float(input(f"Длительность сигнала "))
    hz = int(input(f"Частота "))

    f = lambda x, hz, a: np.sin(2 * np.pi * hz * x) * a

    x = np.linspace(0, t, 256)
    y = f(x, hz, a)

    fig, ax = plt.subplots()

    ax.plot(x, y, "red")
    ax.set_title(f"Частота {hz} Hz, Амплитуда {a}, Длительность сигнала {t} ")

    plt.grid()
    fig.set_figwidth(8)
    fig.set_figheight(6)

    plt.show()
    return a / 2