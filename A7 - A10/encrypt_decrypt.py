'''
Substitution Cipher
Encrypt / Decrypt
'''

def substitute(l, n):
    ret = chr(ord(l) + n)
    if 'a' <= l <= 'z' and ret > 'z':
        ret = chr(ord(ret) - 26)
    elif 'a' <= l <= 'z' and ret < 'a':
        ret = chr(ord(ret) + 26)    

    return ret


def encrypt(text, key):

    if not key:
        raise ValueError("Key cannot be empty.")
    
    temp = ""
    for i in range(len(text)):
        temp += substitute(text[i], ord(key[i % len(key)]) - ord('a'))

    return temp
        

def decrypt(text, key):
    
    if not key:
        raise ValueError("Key cannot be empty.")
    
    temp = ""
    for i in range(len(text)):
        temp += substitute(text[i], ord('a') - ord(key[i % len(key)]))

    return temp