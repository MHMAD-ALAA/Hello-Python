def process(grid) -> list:
    processedGrid = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            sum: int = grid[row][col + 1] + grid[row][col - 1] + grid[row + 1][col] + grid[row - 1][col] + grid[row - 1][col - 1] + grid[row - 1][col + 1] + grid[row + 1][col + 1] + grid[row + 1][col -1]
            if (grid[row][col] == 1 and (sum == 2 or sum == 3)) or (grid[row][col] == 0 and sum == 3):
                processedGrid[row][col] = 1
            else:
                processedGrid[row][col] = 0

    grid = processedGrid[:]
    return grid


if __name__ == '__main__':
    print("Enter the number of columns: ")
    cols: int = int(input())
    print("Enter the number of rows: ")
    rows: int = int(input())

    cols += 2
    rows += 2
    grid = [[0 for i in range(cols)] for j in range(rows)]

    print("Enter the graph: ")
    for row in range(rows - 2):
        # print(f'Enter the Row {row + 1}: ')
        charRow: str = input()
        for col in range(len(charRow)):
            grid[row + 1][col + 1] += (charRow[col] == '#')

    print("Enter the number Of Iterations:")
    Iter = int(input())
    while(Iter):
        Iter -= 1
        grid = process(grid)

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if (grid[row][col] == 1):
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print('=' * (cols - 2))



"""
......
..#...
...#..
.###..
......
......

"""
