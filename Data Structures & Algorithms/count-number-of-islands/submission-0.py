class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 bfs on r and c
        # 2: check r, c from main grid:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        numIsland = 0

        def bfs(row, col):
            # in bfs, look for oher 1's in neighbor
            visited.add((row, col))
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            q.append((row, col))

            while q:
                row, col = q.pop()
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) 
                        and grid[r][c] == "1" 
                    and (r,c) not in visited): 
                        q.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numIsland+=1
                    

        return numIsland


        