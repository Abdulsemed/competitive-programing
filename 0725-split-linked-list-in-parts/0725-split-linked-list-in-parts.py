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
        if size < k:
            while k:
                if temp:
                    val = temp
                    temp = temp.next
                    val.next = None
                    ans.append(val)
                else:
                    ans.append(None)
                k -= 1
        else:
            count = size // k
            remainder = size % k
            while k:
                ans.append(temp)
                for _ in range(count-1):
                    temp = temp.next
                if remainder:
                    temp = temp.next
                    remainder -= 1
                k -= 1
                val = temp.next
                temp.next = None
                temp = val
        return ans