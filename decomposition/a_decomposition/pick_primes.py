

def is_primes(num):
    if num<2:
        return False
    for n in range(2,num):
        if num % n ==0:
            return False
    return True 
        


def pick_primes(list):
    new_list = []
    for num in list:
        prime = is_primes(num)
        if prime:
            new_list.append(num)
    return new_list


print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []