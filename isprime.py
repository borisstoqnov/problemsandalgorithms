def is_prime(a):
    return all(a % i for i in range(2, a))

def is_primsecond(b):

    if b % 2 == 0:
        return False
    for i in range(2,b):
        if b % i == 0:
            return False
    else:
        return True
print(is_primsecond(2833419889721787128217599))