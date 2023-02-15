# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        result = []
        temp = headA
        sets = set()
        while temp:
            sets.add(temp)
            temp = temp.next
        if sets:
            temp2 = headB
            while temp2:
                if temp2 in sets:
                    return temp2
                temp2 = temp2.next
        return None
                
            