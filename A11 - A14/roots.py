def extract_coef(equation):

    if type(equation) != str:
        raise ValueError('Invalid input type. Expecting a String.')
    
    eq = equation.replace(' ' , '')
    a = 0
    b = 0
    c = 0

    if ',' in eq:
        raise ValueError('Invalid equation.')

    if "x2" in eq:
        a =  eq[:eq.index('x2')]
        if a == '' :
            a = str(1)
        elif a == '-':
            a = str(-1)  
    else:
        raise ValueError('Not a Quadratic equation.')
    
    if a == '1' or a == '-1':
        poly_eq = eq.replace('x2' , '')
    else:
        poly_eq = eq.replace(a+'x2' , '')
        
    if 'x' in poly_eq :
        b = poly_eq[:poly_eq.index('x')]
        if b == '+':
            b = '+1' 
            poly_eq = poly_eq.replace('+x' , '')
        elif b == '-':
            b = '-1'
            poly_eq = poly_eq.replace('-x' , '')


    elif not 'x' in poly_eq :
        b = ''

    if c == '':
        c = 0
    else:
        c = poly_eq.replace(b+'x' , '')

    if b == '':
        b = 0
    if c == '':
        c = 0
    return [int(a) , int(b) , float(c)]

def delta(a,b,c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        raise ValueError('Roots are Complex.')
    else:
        return discriminant
    

def quadratic(a,b,c):

    root1 = (-b + (delta(a,b,c)**(0.5)))/(2*a)
    root2 = (-b - (delta(a,b,c)**(0.5)))/(2*a)

    if root1 == root2 == 0.0:
        return [0.0]
    else:
        return [round(root1 , 3), round(root2 , 3)]
   

def roots(equation):

    a = extract_coef(equation)[0]
    b = extract_coef(equation)[1]
    c = extract_coef(equation)[2]

    return quadratic(a,b,c)
    
    