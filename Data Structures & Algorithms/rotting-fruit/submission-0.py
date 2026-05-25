class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if grid is None: 
            return grid

        rows = len(grid)
        cols = len(grid[0])

        # visited and count bad orange and add to que, count fresh orange
        visited = set()
        queue = deque()
        fresh_count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count+=1
                if(grid[i][j] == 2 and (i,j) not in visited):
                    visited.add((i,j))
                    queue.append((i,j))
                    # added source nodes
        if fresh_count == 0:
            return 0
        
        time = 0
        while queue:
            print(f"fresh_count = {fresh_count}")
            print(f"time = {time}")
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc 
                    if( 0<=nr and nr<rows and 0<=nc and nc<cols
                        and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_count-=1

            time+=1
        return -1 if fresh_count else time-1



                
