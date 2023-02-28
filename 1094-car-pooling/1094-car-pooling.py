class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currDist = trips[0][2]
        currPass = 0
        dict1 = {}
        left = 0
        trips.sort(key=lambda trip: trip[1])
        for passg, initial, final in trips:
            for val in dict1:
                if initial >= val:
                    currPass -= dict1[val]
                    dict1[val] = 0
            currPass += passg
            if currPass > capacity:
                return False
            currDist = max(currDist, final)
            dict1[final] = passg + dict1.get(final,0)
        return True