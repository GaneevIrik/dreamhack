def game_desk():
    print("      0  1  2 ")
    print("--------------")
    for i, row in enumerate(field):
        row_str =f" {i} | {' '.join(row)}"
        print(row_str)


def game_move():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue


        if not (cords[0].isdigit() and cords[1].isdigit()):
            print(" Введите числа! ")
            continue

        x, y = map(int, cords)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " -":
            print(" Клетка занята! ")
            continue

        return x, y


def game_winner():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

print("********************")
print("  Добро пожаловать   ")
print("      в игру       ")
print("  крестики-нолики  ")
print("********************")
print("   Вводите:   x y ")
print(" x - номер строки  ")
print(" y - номер столбца ")
field = [[" -"] * 3 for i in range(3)]
series = 0
while True:
    series += 1
    game_desk()
    if series % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = game_move()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if game_winner():
        break

    if series == 9:
        print(" Ничья!")
        break