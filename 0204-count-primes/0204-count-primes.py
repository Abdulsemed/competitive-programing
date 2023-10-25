class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        arr = [True]*(n)
        arr[0] = arr[1] = False
        curr = 2
        while curr * curr < n:
            if arr[curr]:
                j = curr * curr
                while j < n:
                    arr[j] = False
                    j += curr
            curr += 1
        return sum(arr)