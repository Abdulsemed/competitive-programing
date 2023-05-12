class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        dependency = defaultdict(int)
        for greater, lesser in richer:
            graph[greater].append(lesser)
            dependency[lesser] += 1
        queue = deque()
        size = len(quiet)
        ans = [index for index in range(size)]
        for index in range(size):
            if dependency[index] == 0:
                queue.append(index)
        print(graph)
        while queue:
            curr = queue.popleft()
            for child in graph[curr]:
                dependency[child] -= 1
                if dependency[child] == 0:
                    queue.append(child)
                if quiet[ans[child]] > quiet[ans[curr]]:
                    ans[child] = ans[curr]
        return ans