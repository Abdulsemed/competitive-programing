# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def cutter(self,idx,arr):
        currSum = 0
        pos  = -1
        for index in range(idx,len(arr)):
            currSum += arr[index]
            if currSum == 0:
                pos = index
        
        return pos          
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        runner = head
        while runner:
            arr.append(runner.val)
            runner = runner.next
            
        for index in range(len(arr)):
            pos = self.cutter(index,arr)
            if pos != -1:
                for idx in range(index, pos+1):
                    arr[idx] = float("inf")
        newHead = runner = ListNode()
        for index in range(len(arr)):
            if arr[index] != float("inf"):
                runner.next = ListNode(arr[index])
                runner = runner.next     
        return newHead.next