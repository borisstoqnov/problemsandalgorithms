n = 5
a = 0
b = 1
print(a)
print(b)
for i in range(1,n):
    sum = a + pow(b,2)
    a = b
    b = sum
    print(b)