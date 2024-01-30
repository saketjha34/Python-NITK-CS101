"""
Reverse a number
"""

def reverse(number):
    a = str(number)
    empty_list =[]
    if type(number) == int:
        for i in range(len(a)):
            empty_list.append(a[(len(a)-1) - i])
            if '0' in empty_list:
                empty_list.remove('0')
        
        if '-' in empty_list:
            empty_list.remove('-')
            empty_list.insert(0, '-')
            
        result = ''.join(empty_list)
        return int(result)        
    else:
        raise ValueError('Invalid input type. Expecting an integer.')
    

