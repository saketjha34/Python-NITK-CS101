

'''
number of uppercase, lowercase, numerical digits,and other characters in a
string.
'''
def string_composition(input_string):
    uppercase_count = 0
    lowercase_count = 0
    num_count = 0
    oth = 0
    if type(input_string) == str:
        for i in range(len(input_string)):
            if input_string[i].isupper() == True:
                uppercase_count+=1
            elif input_string[i].islower() == True:
                lowercase_count+=1

            elif input_string[i].isdigit() == True:
                num_count+=1
            else:
                oth+=1
                
        return [uppercase_count ,lowercase_count ,num_count ,oth]
    else:
        raise ValueError('Invalid input type. Expecting a String.')

