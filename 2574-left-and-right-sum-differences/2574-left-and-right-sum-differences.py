class Solution:
    def create(self,arr,start,size,inc):
        count = 0
        ans = []
        for index in range(start,size,inc):
            ans.append(count)
            count += arr[index]
        return ans
    def leftRigthDifference(self, num: List[int]) -> List[int]:
        left = self.create(num,0,len(num),1)
        right = self.create(num,len(num)-1,-1,-1)[::-1]
        for index in range(len(num)):
            num[index] = abs(left[index] -right[index])
        return num