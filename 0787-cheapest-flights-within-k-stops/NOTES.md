class Solution:
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
graph  = defaultdict(list)
# dist = {node: float("inf") for node in range(n)}
for a,b,length in flights:
graph[a].append((b, length))
self.dst = dst
self.ans = float("inf")
def dfs(node,stops,curr_dist):
if stops > k:
return
for child, leng in graph[node]:
if stops <= k:
if child == self.dst:
self.ans = min(self.ans, curr_dist + leng)
continue
elif self.ans != float('inf') and self.ans < curr_dist + leng:
continue
dfs(child, stops + 1, curr_dist + leng)
dfs(src,0,0)
if self.ans != float("inf"):
return self.ans
return -1