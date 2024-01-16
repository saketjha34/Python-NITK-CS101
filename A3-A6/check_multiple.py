'''
Check if number divides 7 but not 3
'''


def check_multiple(number):
    if (type(number) == int) and (number >= 0):
        if (number% 7 == 0) and (number % 3 != 0):
            return True
        else:
            return False
    else:
        raise ValueError('input must be aninteger')
          
