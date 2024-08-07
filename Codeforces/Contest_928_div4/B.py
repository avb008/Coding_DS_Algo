t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        s = input()
        grid.append(s)

    previous_row = sum(1 for i in grid[0] if i == "1")
    current_row = 0
    # print(grid, previous_row)

    for j in range(1, n):
        current_row = sum(1 for i in grid[j] if i == "1")
        # print(previous_row, current_row)
        if previous_row and current_row:
            if previous_row != current_row:
                print("TRIANGLE")
                break
            else:
                print("SQUARE")
                break
        previous_row = current_row
