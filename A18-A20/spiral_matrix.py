def spiral_matrix(size):
    
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    
    x, y = 0, 0
    num = 1

    for _ in range(size * size):
        matrix[x][y] = num
        num += 1

        
        new_x, new_y = x + directions[0][0], y + directions[0][1]

        
        if 0 <= new_x < size and 0 <= new_y < size and matrix[new_x][new_y] == 0:
            x, y = new_x, new_y
        else:
            
            directions.append(directions.pop(0))
            x, y = x + directions[0][0], y + directions[0][1]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(num) for num in row))
