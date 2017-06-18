class Node:
    def __init__(self,name):
        self.name = name
        self.edges = []

    def addEdge(self,node):
        self.edges.append(node)




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.addEdge(b)
a.addEdge(c)
b.addEdge(c)
b.addEdge(e)
c.addEdge(g)
d.addEdge(a)
d.addEdge(f)
e.addEdge(f)
e.addEdge(h)


def dep_resolve(node, resolved, unresolved):
    unresolved.append(node)
    for edge in node.edges:
        if edge not in resolved:
            if edge in unresolved:
                raise Exception('Circular reference detected: %s -> %s' % (node.name, edge.name))
            dep_resolve(edge, resolved, unresolved)
    resolved.append(node)
    unresolved.remove(node)

resolved = []
unresolved = []
dep_resolve(c, resolved, unresolved)
for node in resolved:
   print(node.name)