class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # recuerse fn. if found = target, ++
        # bound check
        # recurse over all 4 direction 

        rows = len(board)
        cols = len(board[0])
        count = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = []
        path = set()
        # ALgo is take 1, explore it, find others. have edge cases, have base case, have success return case. length == word length. 

        def dfs(r, c, idx):
            # base case: 
            if idx == len(word):
                return True
                
            if (r<0 or r>= rows 
            or c<0 or c>=cols or
            board[r][c]!= word[idx] or
            (r,c) in path):
                return False
            
            
            path.add((r,c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, idx+1):
                    return True
            path.remove((r,c))

        for row in range(rows):
            for col in range(cols): 
                if dfs(row, col, 0):
                    return True
        
        return False




