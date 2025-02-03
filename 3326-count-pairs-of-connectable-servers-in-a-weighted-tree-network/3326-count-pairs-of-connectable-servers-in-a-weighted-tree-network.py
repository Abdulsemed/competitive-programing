class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        @cache
        def dfs(n, parent):
            temp = []
            for element,weight in dicts[n]:
                if element != parent:
                    weights = dfs(element, n)
                    if n != parent:
                        for w in weights:
                            temp.append(w+weight)
                    else:
                        tempCount = 0
                        for w in weights:
                            if (w + weight) % signalSpeed == 0:
                                tempCount += 1
                        temp.append(tempCount)
                else:
                    temp.append(0)
            return temp

        dicts = defaultdict(list)
        for src,end,weight in edges:
            dicts[src].append([end, weight])
            dicts[end].append([src,weight])
        ans = [0]*(len(edges)+1)
        for index in range(len(ans)):
            temp = dfs(index, index)
            sums = sum(temp)
            for element in temp:
                ans[index] += ((sums- element)*element)
            ans[index] = ans[index]//2

        return ans
