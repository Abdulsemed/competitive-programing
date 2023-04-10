from collections import defaultdict
def addEdge(start, end):
    graph[start].append(end)
    graph[end].append(start)

def vertex(index):
    return graph[index]


nodes = int(input())
query = int(input())
graph = defaultdict(list)
for _ in range(query):
    rows = list(map(int, input().split()))
    if rows[0] == 1: 
        addEdge(rows[1],rows[2])
    else:
        print(*vertex(rows[1]))