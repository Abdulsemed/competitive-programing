class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = list(version1.split("."))
        arr2 = list(version2.split("."))
        
        for index in range(min(len(arr1), len(arr2))):
            if int(arr1[index]) > int(arr2[index]):
                return 1
            elif int(arr1[index]) < int(arr2[index]):
                return -1
        
        left = index+1
        while left < len(arr1):
            if int(arr1[left]):
                return 1
            left += 1
        right = index+1
        while right < len(arr2):
            if int(arr2[right]):
                return -1
            right += 1
        
        return 0
                