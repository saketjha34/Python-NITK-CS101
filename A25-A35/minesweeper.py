def annotate(minefield):
    if not minefield:
        return []

    rows = len(minefield)
    cols = len(minefield[0])

    for row in minefield:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")

    def count_mines(row, col):
        mine_count = 0
        for i in range(max(0, row - 1), min(row + 2, rows)):
            for j in range(max(0, col - 1), min(col + 2, cols)):
                if minefield[i][j] == '*':
                    mine_count += 1
        return mine_count

    result = []
    for i in range(rows):
        new_row = ''
        for j in range(cols):
            if minefield[i][j] == ' ':
                mines_adjacent = count_mines(i, j)
                if mines_adjacent == 0:
                    new_row += ' '
                else:
                    new_row += str(mines_adjacent)
            elif minefield[i][j] == '*':
                new_row += '*'
            else:
                raise ValueError("The board is invalid with current input.")
        result.append(new_row)
    return result

