class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.arr = []
        self.visited = set()
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.arr = [0]*len(labels)
        for src,end in edges:
            self.graph[src].append(end)
            self.graph[end].append(src)
        for val in range(len(labels)):
            if val not in self.visited:
                self.dfs(val,labels,dict())
        return self.arr
    def dfs(self,index,labels,dicts):
        self.visited.add(index)
        if index > len(labels):
            return
        dicts[labels[index]] = 1 + dicts.get(labels[index], 0)
        if index in self.graph:
            for child in self.graph[index]:
                if child not in self.visited:
                    val = dict()
                    self.dfs(child,labels,val)
                    for key in val:
                        dicts[key] = val[key] + dicts.get(key,0)
                
        self.arr[index] = dicts[labels[index]]