class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size = len(mat)*len(mat[0])
        if r * c != size:
            return mat
        else:
            holderList = []
            for index in range(len(mat)):
                for val in range(len(mat[0])):
                    holderList.append(mat[index][val]) 
            newList = []
            index = 0
            for row in range(r):
                lists= []
                for col in range(c):
                    lists.append(holderList[index])
                    index += 1
                newList.append(lists)
    
            return newList
                