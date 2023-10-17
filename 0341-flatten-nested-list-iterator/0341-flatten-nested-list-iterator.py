# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = nestedList
        self.size = len(nestedList)
        self.arr = []
        self.index = 0
        self.curr = -1
        
    def dfs(self,holder):
        if type(holder) == list:
            for element in holder:
                self.dfs(element)
        elif holder.isInteger():
            self.arr.append(holder.getInteger())   
        else:
            self.dfs(holder.getList())
    def next(self) -> int:
        self.curr += 1
        return self.arr[self.curr]
    
    def hasNext(self) -> bool:
        if self.index >= self.size:
            return len(self.arr) > 0 and self.curr < len(self.arr)-1
        else:
            for element in self.nested:
                if element.isInteger():
                    self.arr.append(element)
                else:
                    self.dfs(element)
                self.index += 1
        return len(self.arr) > 0
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())