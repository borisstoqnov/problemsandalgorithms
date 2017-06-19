class MyQUEUE:
    def __init__(self):
        self.holder = []

    def enqueue(self, val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
        except:
            pass
        return val

    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result

graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}



path_queue = MyQUEUE()

def BFS(graph,start,end,q):
    temp_path = [start]
    q.enqueue(temp_path)