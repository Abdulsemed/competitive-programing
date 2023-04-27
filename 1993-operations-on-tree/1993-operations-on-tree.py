class LockingTree:

    def __init__(self, parent: List[int]):
        self.bools = False
        self.locks = [[index,-1] for index in range(len(parent))]
        self.graph = defaultdict(list)
        for index in range(len(parent)):
            self.graph[parent[index]].append(index)
        
    def lock(self, num: int, user: int) -> bool:
        if self.locks[num][1] == -1:
            self.locks[num][1] = user
            return True
        return False
    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num][1] == user:
            self.locks[num][1] = -1
            return True
        return False
    def upgrade(self, num: int, user: int) -> bool:
        self.bools = False
        if self.locks[num][1] == -1 == self.locks[0][1]:
            queue =deque([0])
            while queue:
                curr = queue.popleft()
                if curr == num:
                    self.bools = True
                    break
                for child in self.graph[curr]:
                    if self.locks[child][1] == -1: 
                        queue.append(child)
            
            if not self.bools:
                return False
            self.bools = False
            queue = deque([num])
            while queue:
                curr = queue.popleft()
                if self.locks[curr][1] != -1:
                    self.bools = True
                    break
                for child in self.graph[curr]:
                    queue.append(child)
            if self.bools:
                self.dfs(num)
                self.lock(num,user)
                return True
            return False
        return False
    def dfs(self,num):
        self.locks[num][1] = -1
        if num in self.graph:
            for child in self.graph[num]:
                self.dfs(child)