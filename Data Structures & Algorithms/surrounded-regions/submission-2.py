from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        q = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1. Add all border 'O's to queue and mark them safe
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    q.append((r, c))

        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    q.append((r, c))

        # 2. BFS to mark all 'O's connected to border
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr, nc))

        # 3. Flip surrounded regions and restore safe ones
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
