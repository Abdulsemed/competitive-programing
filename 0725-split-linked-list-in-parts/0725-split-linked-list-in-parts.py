# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        ans = []
        temp = head
        count = size // k
        remainder = size % k
        while k:
            ans.append(temp)
            for _ in range(count):
                val = temp
                temp = temp.next
            if remainder:
                val = temp.next
                temp.next = None
                temp = val
                remainder -= 1
            elif temp:
                val.next = None
                
            k -= 1
            
        return ans