import csv
listofnums = [x for x in range(1,1000000)]
listofnums.append(1239082594078394857)
with open("/home/bobi/filewithnumbers.csv",'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(listofnums)
