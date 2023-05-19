class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dicts = defaultdict(list)
        queue = deque()
        visited = set()
        nums = set()
        flag = False
        for index in range(len(routes)):
            for val in range(len(routes[index])):
                dicts[routes[index][val]].append([index,val])
                if routes[index][val] == source:
                    queue.append((index,val,1))
                    visited.add((index,val))
                    if routes[index][val] == target:
                        return 0   
                if routes[index][val] == target:
                    flag = True
        if not flag: return -1
        while queue:
            currIdx, currVal,level = queue.popleft()
            if currIdx not in nums:
                nums.add(currIdx)
                for val in range(len(routes[currIdx])):
                    if (currIdx,val) not in visited:
                        queue.append((currIdx,val,level))
                        visited.add((currIdx,val))
                    if routes[currIdx][val] == target:
                        return level 
            for row,col in dicts[routes[currIdx][currVal]]:
                if(row,col) not in visited:
                    queue.append((row,col,level+1))
                    visited.add((row,col))
        return -1           