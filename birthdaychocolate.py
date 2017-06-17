####1####
n = 5
s = [1,2,1,3,2]
d = 3
m = 2
count = 0
for i in range(n-m+1):
    if sum(s[i:i+m]) == d:
        count +=1

print(count)

######2######
# pointer = 0
# count = 0
# newlist = []
# while pointer < n:
#     newlist.append(s[pointer])
#     pointer += 1
#     if len(newlist) == m:
#         if sum(newlist) == d:
#             count += 1
#         pointer -= 1
#         newlist = []
# return count