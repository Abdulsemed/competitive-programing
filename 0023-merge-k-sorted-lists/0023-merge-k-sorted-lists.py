# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index in range(len(lists)):
            runner = lists[index]
            while runner:
                heapq.heappush(heap,runner.val)
                runner = runner.next
                
        head = ListNode(0)
        runner = head
        for index in range(len(heap)):
            runner.next = ListNode(heapq.heappop(heap))
            runner = runner.next
        return head.next
        