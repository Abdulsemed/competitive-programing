class Solution:
    def inbound(self,r,c):
        return 0<= r < 2 and 0<= c < 3
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board == [[1,2,3],[4,5,0]]:
            return 0
        queue = []
        for index in range(2):
            for val in range(3):
                if not board[index][val]:
                    queue = deque([[(index,val), board]])
                    visited = {(index,val,tuple(board[0]),tuple(board[1]))}
                    break
            if queue:
                break
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                rc,currBoard = queue.popleft()
                for r,c in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_r = rc[0] + r
                    new_c = rc[1] + c
                    if self.inbound(new_r,new_c):
                        newB = []
                        newB.append(currBoard[0].copy())
                        newB.append(currBoard[1].copy())
                        newB[rc[0]][rc[1]], newB[new_r][new_c] = newB[new_r][new_c], newB[rc[0]][rc[1]]
                        tupleA = tuple(newB[0])
                        tupleB= tuple(newB[1])
                        if (new_r,new_c,tupleA,tupleB) not in visited:
                            visited.add((new_r,new_c,tupleA,tupleB))
                            if newB == [[1,2,3],[4,5,0]]:
                                return level+1
                            queue.append([(new_r,new_c),newB])
                
            level += 1
        return -1