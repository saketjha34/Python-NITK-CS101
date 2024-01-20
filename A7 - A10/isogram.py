"""
Isogram 
"""

def is_isogram(string):
    clean_world =string.lower()

    letter_list = []
    for i in clean_world:
        if i.isalpha():
            if i in letter_list:
                return False
            letter_list.append(i)
    return True

    

        

   


    
