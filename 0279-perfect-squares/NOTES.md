queue = deque([(0,0)])
visited = set()
arr = [1]
curr = 2
while arr[-1] < n:
arr.append(curr*curr)
curr += 1
if arr[-1] > n:
arr.pop()
while queue:
length = len(queue)
for _ in range(length):
val,lev = queue.popleft()
if val == n:
return lev
if (val,lev) in visited:
continue
for ele in arr:
currVal = val + ele
if (currVal,lev+1) not in visited:
queue.append((currVal,lev+1))