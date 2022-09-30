class MinStack(object):

    def __init__(self):
        self.stack=[]
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return None
