class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        max_area = 0
        visited = set()

        def DFS(r,c):
            if(r<0 or c<0 or r>= row or c>=col or
            grid[r][c] !=1 or
            (r,c) in visited):
                return 0

        
            visited.add((r,c))
            area = 0

            directions = [(1,0), (-1, 0), (0,1), (0,-1)]
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]


                area += DFS(nr, nc)

            return 1+ area


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = DFS(r,c)
                    max_area = max(area, max_area)

        return max_area
                