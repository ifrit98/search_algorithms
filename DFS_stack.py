def DFS_stack(graph):
    for vertex in graph:
        vertex.color = WHITE
        vertex.pi = None
    time = 0
    stack = Stack()
    while :
        stack.push(vertex)
