'''
n is a factor of number?
'''


def factor(number, n):
    if type(n) == int and n >= 0:
        if (number % n) == 0:
            return True
            
        else:
            return False
    else:
        raise ValueError('n must be an integer')

    
