class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        moves = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        resultList = []
        queenSet = set()
        for element in queens:
            queenSet.add(tuple(element))
            
        for element in moves:
            row = king[0]
            col = king[1]
            while row > -1 and row < 8 and col >-1 and col < 8:
                row += element[0]
                col += element[1]
                if (row,col) in queenSet:
                    resultList.append([row,col])
                    break
        return resultList