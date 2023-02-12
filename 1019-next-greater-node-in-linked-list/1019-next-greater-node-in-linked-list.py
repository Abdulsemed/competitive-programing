# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        monstack = []
        size = len(vals)
        result = [0]*(size)
        for index in range(size):
            while monstack and vals[monstack[-1]] < vals[index]:
                result[monstack.pop()] = vals[index]
            monstack.append(index)
        return result