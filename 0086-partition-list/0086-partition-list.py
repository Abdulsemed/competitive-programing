# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        header = ListNode(None)
        leastNode = header
        topNode = ListNode(None)
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        temp = head
        while temp.next:
            if temp.next.val < x:
                leastNode.next = temp.next
                temp.next = temp.next.next
                leastNode = leastNode.next
            else:
                temp = temp.next
            if topNode.val is None and temp.val is not None:
                topNode = temp   
        if topNode.val is not None:
            leastNode.next = topNode
        # while temp:
        #     # print(temp.val)
        #     if temp.val >= x:
        #         leastNode.next = temp
        #         break
        #     temp= temp.next
        return header.next
                
                
                