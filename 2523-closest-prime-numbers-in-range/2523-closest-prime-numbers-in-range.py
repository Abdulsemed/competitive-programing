class Solution:
    def sieve(self, size):
        self.bools = []
        
    def closestPrimes(self, left: int, right: int) -> List[int]:
        self.bools = [True] *(right+1)
        self.bools[0] = self.bools[1] = False
        idx = 2
        while idx * idx <= right:
            
            if self.bools[idx]:
                val = idx * idx
                while val <= right:
                    self.bools[val] = False
                    val += idx
                    
            idx += 1
        arr = []
        for index in range(left,right+1):
            if self.bools[index]:
                arr.append(index)
        l_ptr = 0
        r_ptr = 1
        self.bools = [-1,-1]
        minim = float("inf")
        while r_ptr < len(arr):
            val = arr[r_ptr] - arr[l_ptr]
            if val <= 2:
                return [arr[l_ptr], arr[r_ptr]]
            elif val < minim:
                self.bools = [arr[l_ptr], arr[r_ptr]]
                minim = arr[r_ptr] - arr[l_ptr]
            l_ptr += 1
            r_ptr += 1
        return self.bools
        