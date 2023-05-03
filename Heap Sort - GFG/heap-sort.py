class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        while i and arr[i] < arr[(i-1)//2]:
            arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            i = (i-1)//2
        
    def heapify_down(self,arr, n, current):
        while current < n:
            left = 2*current+1
            right = 2*current +2
            pos = current
            if left < n and arr[current] > arr[left]:
                # arr[current], arr[left] = arr[left],arr[current]
                pos = left
            if right < n and arr[pos] > arr[right]:
                # arr[current], arr[right] = arr[right], arr[current]
                pos = right
            arr[pos], arr[current] = arr[current],arr[pos]
            if pos == current:
                break
            current = pos
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        lists = []
        for index in range(n):
            lists.append(arr[index])
            self.heapify(lists,len(lists),index)
        arr = []
        for index in range(n):
            arr.append(lists[0])
            lists[0] = lists[-1]
            lists.pop()
            self.heapify_down(lists,len(lists),0)
        return arr
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        arr[:] = self.buildHeap(arr,n)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends