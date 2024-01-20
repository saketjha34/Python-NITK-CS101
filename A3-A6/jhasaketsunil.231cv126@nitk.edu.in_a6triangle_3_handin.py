"""
Numbers - Triangle example 
"""

def is_triangle(side1, side2, side3):
    if (side1>=0 and side2>=0 and side3>=0):
        if ((side1+side2 >= side3) and (side2+side3 >= side1) and (side1+side3 > side2)):
            return True
        else:
            return False   
    else:
        raise ValueError('Side cannot be negative.')

def is_equilateral(side1, side2, side3):
    if (side1>0 and side2>0 and side3>0):
        if (side1==side2==side3):
            return True
        else:
            return False
    elif(side1 == 0 and side2 == 0 and side3 == 0):
        return False
  
    else:
        raise ValueError('Side cannot be negative.')



def is_isosceles(side1, side2, side3):
    if (side1>=0 and side2>=0 and side3>=0):
        if ((side1+side2 >= side3) and (side2+side3 >= side1) and (side1+side3 > side2)):
            if ((side1==side2) or (side2 == side3) or (side3==side1)):
                return True
            else:
                return False
        else:
            return False   
    else:
        raise ValueError('Side cannot be negative.')

    
    
def is_scalene(side1, side2, side3):
    if (side1>=0 and side2>=0 and side3>=0):
        if ((side1+side2 >= side3) and (side2+side3 >= side1) and (side1+side3 > side2)):
            if ((side1!=side2) and (side2 != side3) and (side3!=side1)):
                return True                 
            else:
                return False
        else:
            return False  
    else:
        raise ValueError('Side cannot be negative.')


def is_degenerate(side1, side2, side3):
    if (side1>0 and side2>0 and side3>0):
        if ((side1+side2 == side3) or (side2+side3 == side1) or (side1+side3 == side2)):
            return True
        else:
            return False  
    elif (side1 == 0 and side2 == 0 and side3 == 0):
        return False
    else:
        raise ValueError('Side cannot be negative.')
print(is_degenerate())
