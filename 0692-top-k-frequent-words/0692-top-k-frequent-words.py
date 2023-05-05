class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicts = {}
        for word in words:
            dicts[word] = 1 + dicts.get(word,0)
        dicts = self.buildHeap(list(dicts.items()),len(dicts.items()),k)
        return dicts
    def heapify(self,arr, n, i):
        while i:
            if arr[i][1] > arr[(i-1)//2][1]:
                arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            elif arr[i][1] == arr[(i-1)//2][1] and arr[i][0] < arr[(i-1)//2][0]:
                arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            else:
                break
            i = (i-1)//2  
    def heapify_down(self,arr, n, current):
        while current < n:
            left = 2*current+1
            right = 2*current +2
            pos = current
            if left < n:
                if arr[current][1] < arr[left][1]:
                    pos = left
                elif arr[current][1] == arr[left][1] and arr[current][0] > arr[left][0]:
                    pos = left
            if right < n:
                if arr[pos][1] < arr[right][1]:
                    pos = right
                elif arr[pos][1] == arr[right][1] and arr[pos][0] > arr[right][0]:
                    pos = right
            arr[pos], arr[current] = arr[current],arr[pos]
            if pos == current:
                break
            current = pos
    def buildHeap(self,arr,n,k):
        lists = []
        for index in range(n):
            lists.append(arr[index])
            self.heapify(lists,len(lists),index)
        arr = []
        for index in range(k):
            arr.append(lists[0][0])
            lists[0] = lists[-1]
            lists.pop()
            self.heapify_down(lists,len(lists),0)
        return arr
        