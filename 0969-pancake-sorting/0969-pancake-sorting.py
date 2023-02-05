class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]: 
        size = max(arr)
        result = []
        while size != 1:
            for index in range(size):
                if arr[index] == size:
                    break
            arr[:index+1] = arr[:index+1][::-1]
            result.append(index+1)
            result.append(size)
            arr[:size] = arr[:size][::-1]
            size -= 1
        print(arr)
        return result
        
                