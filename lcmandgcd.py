# GCD and LCM are not in math module.  They are in gmpy, but these are simple enough:

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

listofn = [10,5,20,30]
result = listofn[0]
for x in listofn:
    result = lcm(result,x)
print(result)
