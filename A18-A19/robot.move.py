def move(input_list):

    x_pos=input_list[0][0]
    y_pos=input_list[0][1]
    route=input_list[1]

    for char in route:
        if char == 'R' :
            x_pos += 1
        elif char == 'L':
            x_pos -= 1
        elif char == 'U':
            y_pos += 1
        elif char == 'D':
            y_pos -= 1
        else:
            raise ValueError("Invalid route direction.")
    return (x_pos, y_pos)

