class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if not board:
        #     return None
        # create edge list
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]


        queue = deque()
        for i in range(rows):
            queue.append((i, 0))
            queue.append((i, cols-1))

        for j in range(cols):
            queue.append((0, j))
            queue.append((rows-1, j))
        
        while queue:
            r, c = queue.popleft()
            if(board[r][c] == "O" and (r,c) not in visited):
                board[r][c] = "S"
                visited.add((r,c))
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (0<=row and row <rows and 0<=col and col<cols and board[row][col] == "O" and (row, col) not in visited):
                        queue.append((row, col))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
                

        


