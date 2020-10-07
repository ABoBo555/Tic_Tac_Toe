# symbols = "         "
# list = []
# for i in range(len(symbols)):
#     list.append(symbols[i])
#
# symbols = [" "," "," "," "," "," "," "," "," "]
symbols = [" " for i in range(9)]
x, y = "", ""
coor = ""
instring = ""
j = 0


def field():
    print('---------')
    for i in range(0, 8, 3):
        print(f"| {symbols[i]} {symbols[i + 1]} {symbols[i + 2]} |")
    print('---------')


def coordinates_():
    global instring
    instring = input("Enter the coordinates: ")


def num_int():
    global x, y
    if not instring[0].isnumeric():
        print("You should enter numbers!")
        coordinates_()
        num_int()
    else:
        x, y = instring.split()
        if not x.isnumeric() or not y.isnumeric():
            print("You should enter numbers!")
            coordinates_()
            num_int()
        elif int(x) > 3 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
            coordinates_()
            num_int()


def run():
    list = [[str(j), str(i)] for i in range(3, 0, -1) for j in range(1, 4)]
    global j
    coor = x + " " + y

    for i in range(len(list)):
        if symbols[i] == 'X' or symbols[i] == 'O':
            list[i] = symbols[i]
        else:
            list[i] = " ".join(list[i])

    if coor not in list:
        print("This cell is occupied! Choose another one!")
        # print(j)
        coordinates_()
        num_int()
        run()
    else:
        for i in range(len(list)):
            #         print(j)
            if "".join(list[i]) == x + " " + y:
                if j == 0:
                    list[i] = "X"
                    symbols[i] = "X"
                    j = 1
                else:
                    list[i] = "O"
                    symbols[i] = "O"
                    j = 0


field()
while True:
    coordinates_()
    num_int()
    run()
    field()
    sym = "".join(symbols)
    x_wins = 'XXX' in [sym[:3], sym[3:6], sym[6:], sym[0:8:3], sym[1:8:3], sym[2:9:3],
                       sym[2:8:2], sym[0:9:4]]
    o_wins = 'OOO' in [sym[:3], sym[3:6], sym[6:], sym[0:8:3], sym[1:8:3], sym[2:9:3],
                       sym[2:8:2], sym[0:9:4]]
    if x_wins:
        print('X wins')
        break
    elif o_wins:
        print('O wins')
        break

    ok = []
    for i in symbols:
        if i == 'X' or i == 'O':
            ok.append(True)
        else:
            ok.append(False)
    if all(ok):
        print('Draw')
        break
