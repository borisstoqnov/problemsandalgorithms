n = "madam"
def palindromea(n):
    return n == n[::-1]

def palindromeb(n):
    word = list(n)
    for letter in word:
        if letter == word[-1]:
            word.pop(-1)
        else:
            return False
    return True

print(palindromeb(n))

