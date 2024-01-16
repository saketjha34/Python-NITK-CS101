"""
Grains on a Chess Board
"""

def square(number):
    if number >=1 and number <=64:
        for i in range(number-1,number):
            return (2**i)
    else:
        raise ValueError('Square number out of range')
       
   
def total():
    c =0
    for i in range(64):
        c += (2**i)
    return c
