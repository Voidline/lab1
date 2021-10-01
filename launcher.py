from imp import function2, function3
from sin import function
from sin2 import function4

if __name__ == "__main__":
    while True:
        print("Меню: Пункт 5.1 - 1 \n"
              "      Пункт 5.2 - 2 \n"
              "      Пункт 6.1 - 3 \n"
              "      Пункт 6.2 - 4 \n"
              "      Пункт 7 - 5 \n"
              "      Пункт 8 - 6 \n"
              "      Выход - 7 \n")
        point = int(input("Выберите пункт: "))
        print()
        if point == 1:
            function()
        if point == 2:
            function(True)
        if point == 3:
            function2()
        if point == 4:
            function3()
        if point == 5:
            function3(True)
        if point == 6:
            function4()
        if point == 7:
            break
