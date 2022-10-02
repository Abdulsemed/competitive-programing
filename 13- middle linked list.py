def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        beg = head
        end = head
        count =0
        while end.next is not None:
            end = end.next
            count += 1
        if count % 2 == 0:
            count = count // 2
        else:
            count = count //2 +1
        while count > 0:
            beg = beg.next
            count -=1
        return beg
