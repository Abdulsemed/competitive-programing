# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftArr = []
        temp = head
        while temp:
            leftArr.append(temp.val)
            temp = temp.next
        arr = leftArr[left-1:right][::-1]
        for index in range(left,right+1):
            leftArr[index-1] = arr[index-left]
        newNode = ListNode(leftArr[0])
        temp = newNode
        size = len(leftArr)
        for index in range(1, size):
            temp.next = ListNode(leftArr[index])
            temp = temp.next
        return newNode
        