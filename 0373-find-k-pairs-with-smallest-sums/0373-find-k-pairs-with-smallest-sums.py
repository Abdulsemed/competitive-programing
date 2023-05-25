class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for index in range(min(len(nums1),k)):
            for val in range(min(len(nums2),k)):
                if len(heap) < k:
                    heapq.heappush(heap,(-(nums1[index]+nums2[val]), nums1[index],nums2[val]))
                else:
                    if nums1[index]+nums2[val] > -heap[0][0]:
                        break
                    else:
                        heapq.heappushpop(heap,(-(nums1[index]+nums2[val]), nums1[index],nums2[val]))
                        
        return [[val1,val2] for _, val1, val2 in heap]
            