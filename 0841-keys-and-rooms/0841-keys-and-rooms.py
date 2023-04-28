class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        children = {0}
        while queue:
            curr = queue.popleft()
            if curr not in children:
                return False
            for element in rooms[curr]:
                if element not in children:
                    children.add(element)
                    queue.append(element)
        if len(children) == len(rooms):
            return True
        return False