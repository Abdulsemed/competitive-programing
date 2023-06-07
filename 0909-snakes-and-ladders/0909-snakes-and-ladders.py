class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        flag = True
        dicts = {}
        for index in range(len(board)-1,-1,-1):
            val = (len(board)) *(len(board) -index)
            if flag:
                val -= (len(board)-1)
            for col in range(len(board)):
                dicts[val] = [(index,col), board[index][col]]
                if flag:
                    val += 1
                else:
                    val -= 1
            flag = not flag
        queue = deque([1])
        visited = {(1)}
        size = len(board)**2
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                ranges = min(curr+6,size)+1
                for val in range(curr+1,ranges):
                    holder = 1
                    if dicts[val][1] != -1:
                        holder = val
                        val = dicts[val][1]
                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
                        visited.add(holder)
                    if val == size:
                        return level + 1
                    
            level += 1
        return -1