class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        arr =[0]
        sums = sum(stones)
        minim = float("inf")
        sets = {0}
        for stone in stones:
            size = len(arr)
            for index in range(size):
                val = arr[index] + stone
                if val not in sets:
                    arr.append(val)
                    sets.add(val)
                    
        for num in arr:
            val = sums - 2*(num)
            if val > -1:
                minim = min(minim, val)
        return minim
    