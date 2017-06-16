def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        temp=a
        a = b
        b = temp%b

#        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
lcmofa = a[0]
for x in a:
    lcmofa = lcm(lcmofa,x)
gcdofb = b[0]
for y in b:
    gcdofb = gcd(gcdofb,y)
print(int(lcmofa))
print(gcdofb)

lcm_copy = lcmofa

count = 0
while lcmofa <= gcdofb:
    if(gcdofb % lcmofa) == 0:
        count += 1
    lcmofa = lcmofa + lcm_copy
print(count)