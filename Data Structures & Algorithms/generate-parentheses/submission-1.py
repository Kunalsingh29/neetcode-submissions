class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = []
    
        left = right = 0
        def addParen(left, right):
            if left == n and right == n:
                res.append(''.join(path))
                return
            if right>left or left>n or right>n:
                return
            
            path.append('(')
            addParen(left+1, right)
            path.pop()

            path.append(')')
            addParen(left, right+1)
            path.pop()

        addParen(0, 0)
        return res
            
            
            
            






        