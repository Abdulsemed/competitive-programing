class Solution:
    def openLock(self, deadends: List[str], target: str) -> int: 
        level = 0
        queue = deque([["0","0","0","0"]])
        visited = {"0000"}
        curr = [element for element in target]
        if "0000" in deadends: 
            return -1
        elif "0000" == target:
            return level
        flag = False
        while queue:
            length = len(queue)
            for _ in range(length):
                if flag: break
                curr = queue.popleft()
                for index in range(4):
                    if flag: break
                    prev = curr[index]
                    for val in [1,-1]:
                        curr[index] = prev
                        if int(curr[index])+val < 0:
                            curr[index] = "9"
                        elif int(curr[index])+val > 9:
                            curr[index] = "0"
                        else:
                            curr[index] = str(int(curr[index])+val)   
                        string = ''.join(curr)
                        if string == target:
                            flag = True
                            queue = []
                            break
                        if string not in deadends and string not in visited:
                            visited.add(string)
                            queue.append(curr[:])
                    curr[index] = prev
            level +=1
        if flag:
            return level   
        return -1