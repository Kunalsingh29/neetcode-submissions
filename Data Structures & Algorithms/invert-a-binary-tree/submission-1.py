# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion after solving current nodes on children nodes. 
        # base case: 
        if root is None: 
            return None
        def invertChild(node:Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return

            # swap children logc: 
            temp  = TreeNode()

            temp = node.left
            node.left = node.right
            node.right = temp
            invertChild(node.left)
            invertChild(node.right)


        invertChild(root)
        return root


    





        