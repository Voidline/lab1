from random import randint

import matplotlib.pyplot as plt
import numpy as np
import json


def function2():
    fig, ax = plt.subplots()

    t = 4
    wd = 0.3
    a = 1

    lim1 = int((t - wd / 2) * 128)
    lim2 = int((t + wd / 2) * 128)
    x = np.linspace(0, 10, 256)
    imp = np.zeros(1280)
    imp[lim1:lim2] = a

    y = []
    for i in range(1280):
        if i % 5 == 0:
            y.append(imp[i])

    plt.plot(x, y, "red")
    plt.grid()
    # ax[i].set_title(f"Частота {hz[i]} Hz, Амплитуда равна {a[i]}")
    plt.title(f"Амплитуда {a}, Центр импульса {t}, Ширина импульса {wd}")

    plt.show()


def function3(upload=False):
    fig, ax = plt.subplots()

    if not upload:
        while True:
            wd = float(input("Ширина импульса "))
            if wd >= 9.9 or wd <= 0:
                print("Неподходящие данные, введите еще раз \n")
            else:
                t = randint(1+int(wd*5), 99-int(wd*5))/10
                break
        a = float(input("Амплитуда "))

        with open("data.json", "w") as file:
            json.dump({"wd": wd, "t": t, "a": a}, file, indent=4)
    else:
        with open("data.json", "r") as file:
            data = json.load(file)
            wd = data["wd"]
            t = data["t"]
            a = data["a"]

    lim1 = int((t - wd / 2) * 128)
    lim2 = int((t + wd / 2) * 128)

    x = np.linspace(0, 10, 256)
    imp = np.zeros(1280)
    imp[lim1:lim2] = a

    y = []
    for i in range(1280):
        if i % 5 == 0:
            y.append(imp[i])

    plt.plot(x, y, "red")
    plt.grid()
    plt.title(f"Амплитуда {a}, Центр импульса {t}, Ширина импульса {wd}")

    plt.show()

