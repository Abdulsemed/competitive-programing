#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(n):
            temp = index
            for val in range(index, n):
                if arr[temp] > arr[val]:
                    temp = val
            if temp != index:
                arr[index], arr[temp] = arr[temp], arr[index]
            self.select(arr,index)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends