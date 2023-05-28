class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        queue = deque([amount])
        level = 0
        visited = set()
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                for val in coins:
                    if curr - val > 0 and curr-val not in visited:
                        visited.add(curr-val)
                        queue.append(curr-val)
                    elif curr - val == 0:
                        return level + 1
            level += 1
        
        return -1