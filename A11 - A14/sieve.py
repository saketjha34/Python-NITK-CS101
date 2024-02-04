'''
Sieve of Eratosthenes
'''
 
def sieve(limit):
    prime_list = []

    if limit < 0:
        raise ValueError('Invalid input.')

    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

