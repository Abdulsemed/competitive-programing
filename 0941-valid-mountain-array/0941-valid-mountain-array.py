class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size = len(arr)-1
        flag = True
        if size <2:
            return False
        for index in range(size):
                if not flag and arr[index] <= arr[index+1]:
                    return False
                elif flag:
                    if arr[index] > arr[index+1]:
                        if index > 0:
                            flag = False    
                        else:
                            return False
                    elif arr[index] == arr[index+1]:
                        return False
        return not flag       
        
            