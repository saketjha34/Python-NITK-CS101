
'''
Raindrops
'''

def convert(number):
    factor_list = [2,3,5,7]
    sounds = ['rim jhim' , 'jal tarang','baadal' , 'chalte hain']
    empty_list = []
    if number < 2:
        raise ValueError('Invalid input.')

    elif (number %2 != 0) and (number %3 != 0) and (number %5 != 0) and (number %7 != 0):
        return number

    else:
        for i in range(len(factor_list)):
            if number % factor_list[i] == 0:
                empty_list.append(sounds[i])    

        result = ' '
        return (result.join(empty_list))



            




    

   

