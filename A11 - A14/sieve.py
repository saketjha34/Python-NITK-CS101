'''
Sieve of Eratosthenes
'''
 
def sieve(limit):
    prime_list = []
    if limit >= 0 :
        for i in range(limit):
            n = 0 
            if i ==1 or i == 0 :
                continue
            else:    
                for j in range(2,i,1):
                    if i % j == 0:
                        n = 1
                        break
                if n == 0:
                    prime_list.append(i)
        return prime_list
    else:
        raise ValueError('Invalid input.')
                    




