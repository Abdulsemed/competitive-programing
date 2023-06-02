class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        first = -1
        second = -1
        for idx in range(2):
            for index in range(len(arr)-1,-1,-1):
                if idx == 0 and index != len(arr)-1:
                    if arr[index+1] < arr[index]:
                        first = index
                        break
                elif idx == 1:
                    if first == -1:
                        break
                    if arr[index] < arr[first]:
                        second = index
                        while index > -1 and arr[index] == arr[second]:
                            second = index
                            index -= 1
                            
                        break
        arr[first], arr[second] = arr[second], arr[first]   
        return arr        