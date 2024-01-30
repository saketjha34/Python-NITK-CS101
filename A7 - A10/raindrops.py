def convert(number):
    factor_list = [2, 3, 5, 7]
    sounds = ['rim jhim', 'jal tarang', 'baadal', 'chalte hain']
    empty_list = []

    if number < 2:
        raise ValueError('Invalid input.')

    has_factors = False
    for i in range(len(factor_list)):
        if number % factor_list[i] == 0:
            empty_list.append(sounds[i])
            has_factors = True

    if not has_factors:
        return str(number)
    else:
        result = ' '.join(empty_list)
        return result


