class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 2147483647:
                    grid[r + dr][c + dc] = grid[r][c] + 1
                    q.append((r + dr, c + dc))

        

    