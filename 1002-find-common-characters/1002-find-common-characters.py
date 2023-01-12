class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        listDict = defaultdict(list)
        size = len(words)
        for index in range(size):
            countDict = {}
            innerSize = len(words[index])
            for value in range(innerSize):
                countDict[words[index][value]] =1 + countDict.get(words[index][value],0)
            for key in countDict:
                listDict[key].append(countDict[key])
        common = []
        for key in countDict:
            if len(listDict[key]) >= size:
                minimum = min(listDict[key])
                for index in range(minimum):
                    common.append(key)
                
        return common