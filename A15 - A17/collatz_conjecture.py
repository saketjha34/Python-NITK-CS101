"""
Collatz Conjecture

How many steps to 1 ? 
If even : divide by 2
If odd : 3x + 1
"""

def steps(number):
    count  = 0 
    if number <= 0 :
        raise ValueError("Only positive numbers are allowed")
    else:
        while number!=1:
            if number % 2 == 0:
                number = number/2
                count +=1           
            elif number %2 != 0:
                number = number*3 +1  
                count+=1
            else:
                continue
        return count

