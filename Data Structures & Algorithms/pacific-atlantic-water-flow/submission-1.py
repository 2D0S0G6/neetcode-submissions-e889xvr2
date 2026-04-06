class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        pacific_visited = set()
        atlantic_visited = set()
        for r in range(rows):
            dfs(r, 0, pacific_visited)
        for c in range(cols):
            dfs(0, c, pacific_visited)

        for r in range(rows):
            dfs(r, cols-1, atlantic_visited)
        for c in range(cols):
            dfs(rows-1, c, atlantic_visited)

        result = list(pacific_visited & atlantic_visited)
        return [list(cell) for cell in result]
