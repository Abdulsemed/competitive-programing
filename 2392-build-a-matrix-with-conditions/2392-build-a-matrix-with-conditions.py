class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        arr = [[0 for _ in range(k)] for _ in range(k) ] 
        
        order = self.conditions(rowConditions,k)
        dicts = {}
        if len(order) != k:
            return []
        for index in range(k):
            arr[index][0] = order[index]
            dicts[order[index]] = index
        order = self.conditions(colConditions,k)
        if len(order) != k:
            return []
        for index in range(k):
            pos = dicts[order[index]]
            arr[pos][0] = 0
            arr[pos][index] = order[index]+1
        return arr
    def conditions(self,arr,k):
        ans = []
        dicts = defaultdict(list)
        inDegree = [0]*(k)
        for start, end in arr:
            dicts[start-1].append(end-1)
            inDegree[end-1] += 1
        queue = deque()
        for index in range(k):
            if inDegree[index] == 0:
                queue.append(index)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in dicts[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)
        return ans
            
        
            