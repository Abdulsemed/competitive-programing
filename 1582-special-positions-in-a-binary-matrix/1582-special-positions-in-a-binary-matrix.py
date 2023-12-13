class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        count =0
        dicts = defaultdict(set)
        for val in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][val] == 1:
                    dicts[val].add((row,val))
        for index in range(len(matrix)):
            ones = 0
            for val in range(len(matrix[0])):
                if matrix[index][val] == 1:
                    ones += 1
            if ones == 1:
                for val in range(len(matrix[0])):
                    if matrix[index][val] == 1:
                        if len(dicts[val]) == 0 or (len(dicts[val]) == 1 and (index,val) in dicts[val]):
                            count += 1
                        
        return count