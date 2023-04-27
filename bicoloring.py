from collections import defaultdict
def color(nodes,size):
    visited = set()
    arr = [0]*(nodes)
    graph = defaultdict(list)
    for _ in range(size):
        src,end = map(int,input().split())
        graph[src].append(end)
        graph[end].append(src)
    for index in range(1,nodes+1):
        if index not in visited:
                color  = 1
                if arr[index] == 1:
                    color = 2
                bools = iterative(index,color,graph,arr,visited)
                if not bools:
                    break           
    if bools:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
def iterative(index,color, graph,arr,visited):
    visited.add(index)
    arr[index-1] = color +1 if color == 1 else 1
    for val in graph[index]:
        if val not in visited:
            arr[val-1] = color
            bools = iterative(val, color+1 if color == 1 else 1, graph,arr,visited)
            if not bools:
                return False
        elif arr[val-1] == arr[index-1]:
            return False
    return True


nodes  = int(input())
while nodes:
    size = int(input())
    color(nodes,size)
    nodes = int(input())