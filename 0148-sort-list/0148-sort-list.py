# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        lists = []
        while runner:
            lists.append(runner.val)
            runner = runner.next
        if lists:
            lists = self.mergesort(lists)
            runner = head
            index = 0
            while runner:
                runner.val = lists[index]
                runner = runner.next
                index += 1
        return head
    def mergesort(self,nums):
        if len(nums) == 1:
            return nums
        size = len(nums)//2
        leftNums = self.mergesort(nums[:size])
        rightNums = self.mergesort(nums[size:])
        left = 0
        right = 0
        leftSize = len(leftNums)
        rightSize = len(rightNums)
        arr = []
        while left < leftSize or right < rightSize:
            val1 = leftNums[left] if left < leftSize else float("inf")
            val2 = rightNums[right] if right < rightSize else float("inf")
            if val1 < val2:
                arr.append(val1)
                left += 1
            else:
                arr.append(val2)
                right += 1
        return arr