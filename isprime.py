def is_prime(a):
    return all(a % i for i in range(2, a))

print(is_prime(33)a)