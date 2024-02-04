'''
Substitute letter
'''
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def substitute(letter, n):
    for i in range(len(alphabets)):
        if alphabets[i] == letter:
            if n > 0:
                return alphabets[(i+n) - (len(alphabets))]
            if n < 0:
                return alphabets[(i+n)]
            else:
                return letter
