class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for index in range(len(equations)):
            graph[equations[index][0]].append([equations[index][1], values[index]])
            graph[equations[index][1]].append([equations[index][0], 1/values[index]])
            
        answer = []
        for src, end in queries:
            if src in graph and src == end:
                answer.append(1)
            elif src in graph and end in graph:
                queue = deque([[1,src]])
                visited = {src}
                flag = False
                while queue:
                    curr_val, node = queue.popleft()   
                    
                    for child, val in graph[node]:
                        if child == end:
                            answer.append(curr_val*val)
                            flag = True
                            break
                        if child not in visited:   
                            queue.append([curr_val * val,child])
                            visited.add(child)
                    if flag:
                        break
                   
                if not flag:
                    answer.append(-1)               
            else:
                answer.append(-1)
        return answer           