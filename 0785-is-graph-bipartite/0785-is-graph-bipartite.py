class Solution:
    def __init__(self):
        self.visited =set()
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        arr= [0]*(size)
        for index in range(size):
            if index not in self.visited:
                color  = 1
                if arr[index] == 1:
                    color = 2
                bools = self.iterative(index,color,graph,arr)
                if not bools:
                    return False
                
        return True
    def iterative(self,index,color, graph,arr):
        self.visited.add(index)
        arr[index] = color +1 if color == 1 else 1
        for val in graph[index]:
            if val not in self.visited:
                arr[val] = color
                bools = self.iterative(val, color+1 if color == 1 else 1, graph,arr)
                if not bools:
                    return False
            elif arr[val] == arr[index]:
                return False
        return True