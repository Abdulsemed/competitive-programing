class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # DFS function to calculate the number of servers in the subtree
        # whose distance from the root is divisible by signalSpeed
        def dfs(node, parent, distance, signalSpeed, adj, count):
            if distance % signalSpeed == 0:
                count[node] = 1
            else:
                count[node] = 0

            for neighbor, weight in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node, distance + weight, signalSpeed, adj, count)
                count[node] += count[neighbor]

        # Function to calculate the number of connectable pairs for a given root
        def calculate_pairs(root, adj, signalSpeed):
            count = {}
            dfs(root, -1, 0, signalSpeed, adj, count)

            total = 0
            S = count[root] - 1  # Exclude the root itself
            subtree_counts = []
            for neighbor, _ in adj[root]:
                if neighbor in count:
                    subtree_counts.append(count[neighbor])

            # Calculate the number of valid pairs
            for i in range(len(subtree_counts)):
                for j in range(i + 1, len(subtree_counts)):
                    total += subtree_counts[i] * subtree_counts[j]

            return total

        # Calculate the result for each server
        result = []
        n = len(edges)+1
        for c in range(n):
            pairs = calculate_pairs(c, adj, signalSpeed)
            result.append(pairs)

        return result