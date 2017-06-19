def isprime(limit):
    limitn = limit+1
    notprime = [False] * limitn
    prime = []
    for i in range(2,limitn):
        if notprime[i]:
            continue
        for j in range(i*2, limitn, i):
            notprime[j] = True
        prime.append(i)
    return prime
print(isprime(10000000))