def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        popped_po = 0
        pushed_po = 0
        while pushed_po <= len(pushed):
            while len(stack) > 0 and stack[-1] == popped[popped_po]:
                stack.pop()
                popped.pop(popped_po)
            if pushed_po <= len(pushed)-1:
                stack.append(pushed[pushed_po])
            pushed_po += 1
        if len(stack)==0:
            return True
        else:
            return False
