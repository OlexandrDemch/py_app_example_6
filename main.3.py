meters = int(input("Введите кол-во метров: "))

what = int(input("Во что вы хотите перевести метры? Мили - 1\n Дюймы - 2\n Ярды - 3"))

if what == 1:

    print(f"{meters} метров = {meters*0.000621} миль")

elif what == 2:

    print(f"{meters} метров = {meters*39.37} дюймов")

elif what == 3:

    print(f"{meters} метров = {meters*1.093613} ярдов")