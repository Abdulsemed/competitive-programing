from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicateDict = defaultdict(list)
        for path in paths:
            files = list(path.split(" "))
            index = len(files)-1
            while index >0:
                right = files[index].index(")")
                left = files[index].index("(")+1
                content = str(files[index][left:right])
#                 location is the path of the file with name 
                location = files[0][:]+"/"+files[index][:left-1]
                duplicateDict[content].append(location)
                index -= 1
        result = []
        for element in duplicateDict.values():
            if len(element) > 1:
                result.append(element)
        return result