# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        runner = head
        arr = []
        while runner:
            arr.append(runner.val)
            runner = runner.next
        temp = 0
        for idx in range(len(arr)-1,-1,-1):
            curr = str((arr[idx]*2)+temp)
            arr[idx] = int(curr[0])
            temp = 0
            if len(curr) >1:
                arr[idx] = int(curr[1])
                temp = int(curr[0])
        index = 0
        runner = head
        before = head
        if temp:
            head.val = temp
            runner = runner.next
        while runner:
            runner.val = arr[index]
            index += 1
            before = runner
            runner = runner.next
        if index < len(arr):
            before.next = ListNode(arr[-1])
            
        return head
            