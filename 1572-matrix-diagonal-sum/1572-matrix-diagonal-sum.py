class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for index in range(len(mat)):
            ans += mat[index][index]
            ans += mat[index][len(mat)-index-1]
            if index == len(mat[index])-index-1:
                ans -= mat[index][index]
        return ans