class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        dicts = {}
        for index in range(len(edges)):
            # graph[edges[index][0]].append(edges[index][1])
            # graph[edges[index][1]].append(edges[index][0])
            dicts[edges[index][0]] = 1 + dicts.get(edges[index][0],0)
            dicts[edges[index][1]] = 1 + dicts.get(edges[index][1],0)
        return sorted(dicts.items(), key = lambda item: item[1], reverse = True)[0][0]