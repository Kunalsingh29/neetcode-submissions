"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given node: 
        # from this node, travel all other nodes.
        # understand tha node is justa label or reference to object. 
      
      # clone graph: we will use DFS now: 
        if not node: 
            return None
        clone_map = {}

        def dfs(node):
            if node in clone_map:
                # this is clone of node
                return clone_map[node]
            # create node and add neighbors: 
            curr_node = Node(node.val)
            clone_map[node] = curr_node

            for neighbor in node.neighbors:
                curr_node.neighbors.append(dfs(neighbor))
            
            return curr_node


        dfs(node)

        return clone_map[node]


    
