# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        runner = list1
        while runner and count < a-1:
            runner = runner.next
            count += 1
        newRunner = runner.next    
        runner.next = list2
        
        while newRunner and count < b:
            count += 1
            newRunner = newRunner.next
            
        runner = runner.next
        while runner.next:
            runner = runner.next
        runner.next = newRunner
        
        return list1
        
            
        