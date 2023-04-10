from collections import defaultdict
def sands(size):
    graph = set()
    sources = []
    sinks = []
    for index in range(size):
        rows = list(map(int, input().split()))
        for j in range(len(rows)):
            if rows[j] == 1:
                graph.add(j)

        if not 1 in rows:
            sinks.append(index+1)
    for index in range(size):
        if index not in graph:
            sources.append(index+1)

    print(len(sources), *sorted(sources))
    print(len(sinks), *sorted(sinks))


size = int(input())
sands(size)