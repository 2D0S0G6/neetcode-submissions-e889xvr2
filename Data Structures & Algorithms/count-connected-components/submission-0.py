class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        components = 0

        for i in range(n):
            if i not in visited:
                components += 1
                stack = [i]

                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    visited.add(node)

                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        return components
