
graph = {'A': ['B', 'C', 'E'],
             'B': ['C', 'D','H'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C', 'G'],
             'H': ['']}



def bfs(graph,start,end):

    queue = [start]
    visited = [start]
    path = []
    tmp_path = []
    while queue:
        currentpoint = queue.pop(0)

        path.append(currentpoint)
        print(currentpoint)
        for node in graph.get(currentpoint):
            if node not in visited:
                visited.append(node)
                queue.append(node)
            if node == end:
                path.append(node)
                return path

        #print(path)

    # enque all the neighbours of the node
    # pop the first one add to visited, make a path from each neighbour when we have each make a new queue from the next node in neighbours
    # while queue:
    #     path = queue.pop(0)
    #     nodes = path
    #     for i in

print(bfs(graph,"A","G"))