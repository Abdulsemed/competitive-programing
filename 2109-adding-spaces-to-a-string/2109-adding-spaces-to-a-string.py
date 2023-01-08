class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left = 0
        right = spaces[0]
        stringList = [s[left:right], " "]
        size = len(spaces)
        for index in range(1,size):
            left = right
            right = spaces[index]
            stringList.append(s[left:right])
            stringList.append(" ")
        stringList.append(s[right:])   
        return ''.join(stringList)