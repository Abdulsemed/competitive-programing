class Solution:
    def racecar(self, target: int) -> int:
        if target == 1:
            return 1
        queue = deque([("A",1,2)])
        level = 2
        visited = {("A",1,2)}
        while queue:
            length  = len(queue)
            for _ in range(length):
                curr,position,speed = queue.popleft()
                for choice in ["A","R"]:
                    newPos = position
                    if choice == "A":
                        newPos = position+ speed
                        newSpeed = speed * 2
                    elif speed < 0:
                        newSpeed = 1
                    else:
                        newSpeed = -1
                    if (choice,newPos,newSpeed) not in visited:
                        queue.append((choice,newPos,newSpeed))
                        visited.add((choice,newPos,newSpeed))
                    if newPos == target:
                        return level
            level += 1
        
                        
                            