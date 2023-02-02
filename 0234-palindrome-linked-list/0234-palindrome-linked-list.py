# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        fast = head
        if fast.next:
            while fast.next and fast.next.next:
                temp = temp.next
                fast = fast.next.next
            right = temp.next
            if fast.next:
                temp  = temp.next
            prev = None
            current = head
            while(current is not temp):
                Next = current.next
                current.next = prev
                prev = current
                current = Next
            temp = prev
            while right:
                if temp.val != right.val:
                    return False
                right = right.next
                temp = temp.next
            
        return True     