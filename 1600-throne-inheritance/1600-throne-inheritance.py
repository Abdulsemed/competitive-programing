class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inherit = defaultdict(list)
        self.inherit[kingName] = []
        self.visited = set()
        self.name = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.inherit[parentName].append(childName)

    def death(self, name: str) -> None:
        self.visited.add(name)
    def dfs(self,name,path,arr):
        if name not in self.visited:
            arr.append(name)
        if name in self.inherit:
            for child in self.inherit[name]:
                self.dfs(child,path,arr)

    def getInheritanceOrder(self) -> List[str]:
        arr=[]
        self.dfs(self.name,set(),arr)
        
        return arr


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()