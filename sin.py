import random
import matplotlib.pyplot as plt
import numpy as np


def function(ramp=False):
    fig, ax = plt.subplots(3)
    hz = [1, 10, 50]

    if ramp:
        a = [random.randint(1, 10) for i in range(3)]
    else:
        a = [int(input(f"Введите амплитуду ({i + 1}/3): ")) for i in range(3)]

    for i in range(3):

        x = np.linspace(0, 1, 256)
        y = [np.sin(2*np.pi*t * hz[i]) * a[i] for t in x]
        ax[i].plot(x, y, "red")
        ax[i].grid()
        ax[i].minorticks_on()
        ax[i].set_title(f"Частота {hz[i]} Hz, Амплитуда равна {a[i]}")
        fig.set_figwidth(10)
        fig.set_figheight(8)

    plt.show()





