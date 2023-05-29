class Solution:
    def __init__(self):
        self.reps = {}
        self.size ={}
        self.directions = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]
    def inbound(self,row,col,r,c):
        return 0<= row<= r and 0<= col <= c
    def find(self,node):
        if node != self.reps[node]:
            self.reps[node] = self.find(self.reps[node])
        return self.reps[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return True
        elif self.size[rep1] > self.size[rep2]:
            self.reps[rep2] = rep1
            self.size[rep1] += self.size[rep2]
        else:
            self.reps[rep1] = rep2
            self.size[rep2] += self.size[rep1]
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = set()
        right = set()
        visited = set()
        for child in cells:
            self.reps[(child[0], child[1])] = (child[0], child[1])
            self.size[(child[0], child[1])] = 1
        for index in range(len(cells)):
            visited.add((cells[index][0],cells[index][1]))
            if cells[index][1] == 1:
                left.add(((cells[index][0],cells[index][1])))
            elif cells[index][1] == col:
                right.add(((cells[index][0],cells[index][1])))
            for r,c in self.directions:
                new_r = cells[index][0]+r
                new_c = cells[index][1] + c
                if self.inbound(new_r,new_c,row,col) and (new_r,new_c) in visited:
                    self.union((cells[index][0],cells[index][1]),(new_r,new_c))
            lefts,rights = set(),set()
            for element in left:
                lefts.add(self.find(element))
            for element in right:
                rights.add(self.find(element))
            for val in lefts:
                if val in rights: return index
        return len(cells)       