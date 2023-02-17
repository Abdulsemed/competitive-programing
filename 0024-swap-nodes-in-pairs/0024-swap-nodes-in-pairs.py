# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        newNode = ListNode(0,head)
        prev = newNode
        if head and head.next:
            runner = head.next
            while temp and runner:
                prev.next = runner
                temp.next = runner.next
                runner.next = temp

                prev = prev.next.next
                temp = temp.next
                if temp:
                    runner = temp.next           
        return newNode.next