class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: 
            return heights
        rows =len(heights)
        cols = len(heights[0])


        # pacific list 
        queue_p = deque()
                # atlantic list 
        queue_a = deque()

        valid_p = set()
        valid_a = set()
        for i in range(rows):
            queue_p.append((i, 0))
            valid_p.add((i,0))
            queue_a.append((i, cols-1))
            valid_a.add((i, cols-1))
        for j in range(cols):
            queue_p.append((0, j))
            valid_p.add((0,j))
            queue_a.append((rows-1, j))
            valid_a.add((rows-1, j))
        
        # list done: start BF90,-1,S on both from the queue. add elements to a set of valid points
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(queue, valid):
            while queue:
            
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if(row>=0 and row<rows and col>=0 and col<cols and (row, col) not in valid and heights[row][col] >=heights[r][c]):
                        valid.add((row, col))
                        queue.append((row, col))

        bfs(queue_p, valid_p)
        bfs(queue_a, valid_a)

        return list(valid_p.intersection(valid_a))