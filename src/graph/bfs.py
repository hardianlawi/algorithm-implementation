from queue import Queue


def bfs(g, N, s):
    """Perform Breadth-first search on a Graph starting from start node s

    Args:
        g (graph.Graph): graph to perform the BFS
        N (int): number of nodes in the graph
        s (int): start node
    """
    visited = [False]
    queue = Queue(0)
    queue.put(s)
    while len(queue) != 0:
        temp = queue.get()

    return
