'''
Fixed Substitute
'''
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def f_substitute(letter):
    for i in range(len(alphabets)):
        if  alphabets[i] == letter:
            return alphabets[(i+5) - len(alphabets)]
       
  
