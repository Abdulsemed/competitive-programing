class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        arr = [True for i in range(n)]
        arr[0] = arr[1] = False
        curr = 2
        sets = set()
        while curr * curr < n:
            if arr[curr]:
                j = curr * curr
                while j < n:
                    arr[j] = False
                    sets.add(j)
                    j += curr
            curr += 1
        return n-len(sets)-2