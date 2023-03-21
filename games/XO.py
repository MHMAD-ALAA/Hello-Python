
if __name__ == '__main__':
    grid = [[' ' for i in range(5)] for j in range(3)]
    for row in range(3):
        for col in range(5):
            if (col & 1):
                grid[row][col] = '|'

    row1 = row2 = row3 = col1 = col2 = col3 = mainDia = antiDia = length = 0
    turn: int = -1
    while 1:
        length += 1
        if (turn < 0):
            print("X"); turn = 1
        else:
            print("O"); turn = -1

        row = col = 0
        move: str = input()
        if move == 'top-L':
            row1 += turn; col1 += turn; mainDia += turn; row = 0; col = 0;
        elif move == 'top-M':
            row1 += turn; col2 += turn; row = 0; col = 2
        elif move == 'top-R':
            row1 += turn; col3 += turn; antiDia += turn; row = 0; col = 4
        elif move == 'mid-L':
            row2 += turn; col1 += turn; row = 1; col = 0
        elif move == 'mid-M':
            row2 += turn; col2 += turn; mainDia += turn; antiDia += turn; row = 1; col = 2
        elif move == 'mid-R':
            row2 += turn; col3 += turn; row = 1; col = 4
        elif move == 'low-L':
            row3 += turn; col1 += turn; antiDia += turn; row = 2; col = 0
        elif move == 'low-M':
            row3 += turn; col2 += turn; row = 2; col = 2
        elif move == 'low-R':
            row3 += turn; col3 += turn; mainDia += turn; row = 2; col = 4

        if turn == 1:
            grid[row][col] = 'X'
        else:
            grid[row][col] = 'O'

        ans: list = {row1, row2, row3, col1, col2, col3, mainDia, antiDia}

        for row in range(3):
            for col in range(5):
                print(grid[row][col], end='')
            print()
            if (row < 2): print("-+-+-")

        if (3 in ans):
            print("X-Wins")
            break
        elif (-3 in ans):
            print("O-Wins")
            break
        elif (length == 9):
            print("SETTELMATE")
            break


