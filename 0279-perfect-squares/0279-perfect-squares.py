class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([(0,0)])
        visited = set()
        arr = [1]
        curr = 2
        while arr[-1] < n:
            arr.append(curr*curr)
            curr += 1
        if arr[-1] > n:
            arr.pop()
        arr = arr[::-1]
        while queue:
            length = len(queue)
            for _ in range(length):
                val,lev = queue.popleft()
                if (val,lev) in visited:
                    continue
                    
                for ele in arr:
                    currVal = val + ele
                    if (currVal,lev+1) not in visited and currVal < n:
                        queue.append((currVal,lev+1))
                    if currVal == n:
                        return lev+1