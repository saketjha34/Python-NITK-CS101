'''
CS101. W2 - Numbers.
The Mysore Pak Cookbook 
'''

# insert the value 
EXPECTED_COOK_TIME= 40

def cooking_time_remaining(elapsed_cooking_time):
    """Calculate the cooking time remaining.

    :param elapsed_cooking_time: int cooking time already elapsed.
    :return: int remaining cooking time derived from 'EXPECTED_COOK_TIME'.

    Function that takes the actual minutes the Mysore Pak has been in the cooking pan
    on fire as an argument and returns how many minutes the sweet still needs to cook
    based on the `EXPECTED_COOK_TIME`.
    """

    return 40 - elapsed_cooking_time

def preparation_time_required_in_minutes(num_pieces):
    """
    Calculate preparation time for the given number of pieces
    Preparation time is (num_pieces // BATCH_SIZE) * PREPARATION_TIME

    Assumption: num_pieces % 10 == 0 always
    """
    if (num_pieces % 10 ==0) and (num_pieces > 0):
        return (num_pieces/10)*5    
    else:
        raise ValueError('Zero pieces not allowed')

    
def remaining_time_in_minutes(num_pieces, elapsed_time):
    """
    Two parameters:
    num_pieces: number of Mysore Pak pieces being prepared
    elapsed_cooking_time: the number of minutes elapsed from start till now

    Returns the number of minutes remaining till all the
    Mysore Paks are fully done.
    """
    if (elapsed_time <= (EXPECTED_COOK_TIME + (cooking_time_remaining(elapsed_cooking_time=30)))):
        return EXPECTED_COOK_TIME+ (cooking_time_remaining(elapsed_cooking_time=30))-(elapsed_time)
    else:
        return 0


