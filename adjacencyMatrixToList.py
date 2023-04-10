from collections import defaultdict
def converter(size):
    graph = defaultdict(list)
    for index in range(size):
        rows = list(map(int, input().split()))
        for val in range(len(rows)):
            if rows[val] == 1:
                graph[index].append(val+1)
    for index in range(size):
        print(len(graph[index]), *graph[index])




size = int(input())
converter(size)