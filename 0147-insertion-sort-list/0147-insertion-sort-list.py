# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp= head.next
        runner = head
        starter = ListNode(None,head)
        head = starter
        while temp:
            last = temp.next
            if runner.val > temp.val:
                starter = head
                while starter.next and starter.next.val < temp.val:
                    starter = starter.next
                runner.next = last
                temp.next = starter.next
                starter.next = temp
            else:
                runner = runner.next
            temp = last
        return head.next