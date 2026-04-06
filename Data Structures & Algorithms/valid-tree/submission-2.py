class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 :
            return False
        adj = {i:[] for i in range(n)} 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        stack = [(0,-1)]
        while stack:
            node,parent = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor!=parent:
                    stack.append((neighbor,node))

        return len(visited) == n