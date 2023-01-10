class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        moves = []
        for index in range(size):
            count = 0
            for values in range(size):
                if boxes[values] == "1":
                    count += abs(values-index)
            moves.append(count)
            
        return moves