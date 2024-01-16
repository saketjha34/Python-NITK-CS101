"""
nth root of a number
"""

def nth_root(number, n):
    if n > 0:
        return round(number**(1/n),2)
    else:
        raise ValueError('Negative roots can\'t be calculated')