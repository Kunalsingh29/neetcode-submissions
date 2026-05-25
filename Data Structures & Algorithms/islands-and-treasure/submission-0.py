class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: 
            return grid
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()


        # adding source nodes to queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i,j) not in visited: 
                    visited.add((i,j))
                    queue.append((i,j))

        # source nodes added 
        # now traverse staarting formt these and increment distance. 
        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    # if next neighbor is valid, change dist to 1
                    r = row + dr
                    c = col + dc
                    if(0<=r and r<rows and 0<=c and c<cols and (grid[r][c] == 2147483647) and (r,c) not in visited):
                        grid[r][c] = distance+1
                        visited.add((r,c))
                        queue.append((r,c))
                
            distance+=1

    