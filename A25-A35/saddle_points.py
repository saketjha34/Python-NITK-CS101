def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    saddle_points = []
    
    for i, row in enumerate(matrix):
        for j, point in enumerate(row):
            row_max = max(row)
            col_min = min(matrix[k][j] for k in range(len(matrix)))
            
            if point == row_max and point == col_min:
                saddle_points.append({"row": i + 1, "column": j + 1})
    
    return saddle_points

    
