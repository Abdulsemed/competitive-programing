# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newNode = ListNode(-1,head)
        temp = newNode
        count =k-1
        for _ in range(k-1):
            temp = temp.next
        runner = temp
        while runner:
            runner = runner.next
            count += 1
        runner = newNode
        count -= k+1
        for _ in range(count):
            runner = runner.next
        if count < k:
            temp, runner = runner, temp
        prev = temp.next
        last = runner.next.next
        temp.next = runner.next
        if prev.next != runner.next:
            temp.next.next = prev.next
        else:
            temp.next.next = runner
        runner.next = prev
        runner.next.next = last
        return newNode.next
        