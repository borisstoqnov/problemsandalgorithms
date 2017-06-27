
graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}

queue = []


for i in graph.get("A"):
    queue.append(i)

while queue:
    print(queue.pop())