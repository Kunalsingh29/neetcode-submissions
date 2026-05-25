class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cound edges and then count visited nodes:
        edge_count = len(edges)
        if edge_count != n-1:
            return False
        
        adj_list = [[] for _ in range(n)]
        visited = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for n in adj_list[node]:
                if n not in visited: 
                    dfs(n)

        dfs(0)
        return n == len(visited)


