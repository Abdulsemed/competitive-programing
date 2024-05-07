# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(100000)
        val = 0
        runner = head
        while runner:
            val = (val*10) + runner.val
            runner = runner.next
            
        strs = str(2*val)
        index = 0
        runner = head
        before = head
        while runner:
            runner.val = int(strs[index])
            index += 1
            before = runner
            runner = runner.next
        if index <len(strs):
            before.next = ListNode(int(strs[index]))
            
        return head
            