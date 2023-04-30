class Solution:
    def openLock(self, deadends: List[str], target: str) -> int: 
        level = 0
        queue = deque(["0000"])
        visited = {"0000"}
        if "0000" in deadends: 
            return -1
        elif "0000" == target:
            return level
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr == target:
                    return level
                for index in range(4):
                    for val in [1,-1]:
                        num = int(curr[index])+val
                        if num < 0:
                            holder  = "9"
                        elif num > 9:
                            holder = "0"
                        else:
                            holder = str(num)   
                        string = curr[:index]+holder+curr[index+1:]
                        if string not in deadends and string not in visited:
                            visited.add(string)
                            queue.append(string)
            level +=1
        return -1