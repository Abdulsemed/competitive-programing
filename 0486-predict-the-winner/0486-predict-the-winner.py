class Solution:
    def predict(self,arr,l,r,bools):
        if l== r:
            if bools:
                return [arr[l],0]
            return [0,arr[l]]
        
        if bools:
            right = self.predict(arr,l,r-1,not bools)
            right[0] += arr[r]
            left = self.predict(arr,l+1,r,not bools)
            left[0] += arr[l]
            if right[0]>= left[0]:
                return right
            else:
                return left
        else:
            right = self.predict(arr,l,r-1,not bools)
            right[1] += arr[r]
            left = self.predict(arr,l+1,r,not bools)
            left[1] += arr[l]
            if right[1] >= left[1]:
                return right
            else:
                return left
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.predict(nums,0,len(nums)-1,True)
        return score[0] >= score[1]