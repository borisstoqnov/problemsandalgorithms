import time
import csv
with open("/home/bobi/filewithnumbers.csv",'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    numbers = [x for x in reader]
start = time.time()

def checkfirstrepeating(numbers):


    repeating = []
    for i in range(len(numbers)):
        if (numbers[i] in repeating or numbers[i] in numbers[i+1:]):
            repeating.append(numbers[i])

        else:
            return numbers[i]

def fn(s):
  order = []
  counts = {}
  for x in s:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
      order.append(x)
  for x in order:
    if counts[x] == 1:
      return x
  return None

print(checkfirstrepeating(numbers))


#print(fn(numbers))
end = time.time()
print(end - start)