from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def hasCycle(self,index,graph,colors,visited):
        if colors[index] == 1:
            return False
        if colors[index] == 2:
            return True
        colors[index] = 1
        for child in graph[index]:
            if (index,child) not in visited and (child,index) not in visited:
                visited.add((index,child))
                if not self.hasCycle(child,graph,colors,visited):
                    return False
        colors[index] = 2
        return True
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:  
        #Code here
        colors = [0]*(V)
        visited = set()
        for index in range(V):
            if not self.hasCycle(index,adj,colors,visited):
                return 1
        return 0

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends