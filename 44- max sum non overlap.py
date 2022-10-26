def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        count = 0
        fir_sum = [0]*(len(nums))
        sec_sum = [0]*(len(nums))
        for i, elt in enumerate(nums):
            count += elt
            if i+1 - firstLen >= 0:
                fir_sum[i+1-firstLen] = count
                count -= nums[i+1-firstLen]
        count = 0
        for i, elt in enumerate(nums):
            count += elt
            if i+1 - secondLen >= 0:
                sec_sum[i+1-secondLen] = count
                count -= nums[i+1-secondLen]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j >= i and j < i + firstLen: continue
                if i >= j and i < j + secondLen: continue
                if j+secondLen > i and j+firstLen <= i + firstLen: continue
                if i + firstLen > j and i +firstLen <= j + secondLen: continue
                count = max(count, fir_sum[i]+sec_sum[j])
           
        return count
