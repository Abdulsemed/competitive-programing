class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        rear = 0
        seconds= 0
        size = len(tickets)
        others = 0
        while tickets[k] > 0:
            if rear == k:
                seconds += others+1
                tickets[k] -= 1
                others = 0
            elif tickets[rear] > 0:
                others += 1
                tickets[rear] -= 1
            rear += 1
            rear = rear % size
        return seconds
            
                