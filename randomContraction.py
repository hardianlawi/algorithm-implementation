import random

def randomContraction(graph):

    while len(graph) > 2:

        v = random.choice(list(graph.keys()))
        w = random.choice(list(graph[v]))

        if not isinstance(v, tuple):
            v = (v,)

        if w in graph:
            new_key = v + (w,)
        else:
            for key in graph:
                if isinstance(key, tuple):
                    if w in key:
                        new_key = v + key
                        w = key
                        break

        if len(v) == 1:
            v = v[0]

        graph[new_key] = graph.pop(v) + graph.pop(w)

        graph[new_key] = [x for x in graph[new_key] if x not in new_key]

    return graph

        # graph[tmp] = graph.pop(tmp[0], []) + graph.pop(tmp[1], [])


if __name__ == "__main__":

    graph = {}
    graph['1'] = ['2', '4']
    graph['2'] = ['1', '3', '4']
    graph['3'] = ['2', '4']
    graph['4'] = ['1', '2', '3']

    # graph = dict()
    # tmp = input("Input vertices: \n").strip()
    # while tmp != '':
    #     graph[tmp] = []
    #     tmp = input().strip()

    # tmp = input("Input edges: \n").strip()
    # while tmp != '':
    #     tmp = tmp.split()
    #     graph[tmp[0]].append(tmp[1])
    #     graph[tmp[1]].append(tmp[0])
    #     tmp = input().strip()

    print(randomContraction(graph))
