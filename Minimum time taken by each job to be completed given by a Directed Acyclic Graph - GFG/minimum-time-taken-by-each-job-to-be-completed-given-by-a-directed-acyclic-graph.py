from typing import List


from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        ans = ["0"]*(n)
        graph = defaultdict(list)
        degree = defaultdict(int)
        for src, end in edges:
            graph[src-1].append(end-1)
            degree[end-1] += 1
        queue =deque()
        for index in range(n):
            if degree[index] == 0:
                queue.append(index)
        while queue:
            curr = queue.popleft()
            ans[curr]  = str(int(ans[curr]) + 1)
            for child in graph[curr]:
                degree[child] -= 1
                ans[child] = str(max(int(ans[curr]), int(ans[child])))
                if degree[child] == 0:
                    queue.append(child)
        
        return " ".join(ans)


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends