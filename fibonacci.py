# n = 5
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(1,n):
#     sum = a + pow(b,2)
#     a = b
#     b = sum
#     print(b)

##The python way
def fib(n):
    a, b = 0, 1
    for i in range(1,n):            # First iteration:
        print(a)            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
fib(25)