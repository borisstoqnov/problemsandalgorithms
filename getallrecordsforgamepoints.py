numberofgames = 9
games = [10, 5, 20, 20, 4, 5, 2, 25, 1]
countbest = 0
countworst = 0
bestrecord = games[0]
worstrecord = games[0]

for x in games:
    if x > bestrecord:
        countbest +=1
        bestrecord = x
    if x < worstrecord:
        countworst += 1
        worstrecord = x
print(countbest,countworst)