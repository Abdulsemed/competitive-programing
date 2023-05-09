class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index in range(len(tasks)):
            tasks[index] = [tasks[index][0],tasks[index][1],index]
        heapq.heapify(tasks)
        _,curr,index = heapq.heappop(tasks)
        ans = []
        heap = []
        counter = _
        while tasks or heap:
            counter += curr
            if not heap and tasks and  counter < tasks[0][0]:
                counter = tasks[0][0]
            while tasks and counter >= tasks[0][0]:
                _,val,idx = heapq.heappop(tasks)
                heapq.heappush(heap,[val,idx])
            ans.append(index)
            curr,index = heapq.heappop(heap)
        ans.append(index)  
        return ans         
                