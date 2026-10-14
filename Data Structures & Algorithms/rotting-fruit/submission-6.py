class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1