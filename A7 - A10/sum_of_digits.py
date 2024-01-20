"""
Sum of digits
"""

def sum_of_digits(number):
    sum = 0
    if (number > 0) and (type(number) != float):
        for i in str(number):
            sum += int(i)
        return sum
    else:
        raise ValueError('Invalid input type. Expecting an integer.')