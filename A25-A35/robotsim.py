# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, route):
        for instruction in route:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()

    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH

    def advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        elif self.direction == WEST:
            self.coordinates = (x - 1, y)

# Test cases
# robot = Robot(NORTH, 0, 0)
# robot.move("R")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) EAST

# robot = Robot(EAST, 0, 0)
# robot.move("R")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) SOUTH

# robot = Robot(SOUTH, 0, 0)
# robot.move("R")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) WEST

# robot = Robot(WEST, 0, 0)
# robot.move("R")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) NORTH

# robot = Robot(NORTH, 0, 0)
# robot.move("L")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) WEST

# robot = Robot(WEST, 0, 0)
# robot.move("L")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) SOUTH

# robot = Robot(SOUTH, 0, 0)
# robot.move("L")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) EAST

# robot = Robot(EAST, 0, 0)
# robot.move("L")
# print(robot.coordinates, robot.direction)  # Output: (0, 0) NORTH

# robot = Robot(NORTH, 0, 0)
# robot.move("A")
# print(robot.coordinates, robot.direction)  # Output: (0, 1) NORTH

# robot = Robot(SOUTH, 0, 0)
# robot.move("A")
# print(robot.coordinates, robot.direction)  # Output: (0, -1) SOUTH

# robot = Robot(EAST, 0, 0)
# robot.move("A")
# print(robot.coordinates, robot.direction)  # Output: (1, 0) EAST

# robot = Robot(WEST, 0, 0)
# robot.move("A")
# print(robot.coordinates, robot.direction)  # Output: (-1, 0) WEST

# robot = Robot(NORTH, 7, 3)
# robot.move("RAALAL")
# print(robot.coordinates, robot.direction)  # Output: (9, 4) WEST

# robot = Robot(NORTH, 0, 0)
# robot.move("LAAARALA")
# print(robot.coordinates, robot.direction)  # Output: (-4, 1) WEST

# robot = Robot(EAST, 2, -7)
# robot.move("RRAAAAALA")
# print(robot.coordinates, robot.direction)  # Output: (-3, -8) SOUTH

# robot = Robot(SOUTH, 8, 4)
# robot.move("LAAARRRALLLL")
# print(robot.coordinates, robot.direction)  # Output: (11, 5) NORTH
