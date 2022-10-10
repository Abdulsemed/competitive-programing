def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        beg = head
        end = head  
        if end is not None:
            while end.next is not None:
                if end.val == end.next.val:
                    while end.next is not None and end.val == end.next.val:
                        end = end.next
                    while beg.next.val != end.val:
                            beg = beg.next
                    if end.next is None and beg.val != end.val:
                        beg.next = None
                    elif end.next is not None and beg.val != end.val:
                        beg.next = end.next
                        end = end.next
                    elif end.next is not None:
                        head = end.next
                        beg =head
                        end =head
                    else:
                        head = None
                 
                else:
                    end = end.next
        return head
