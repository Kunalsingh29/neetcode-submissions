class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list, do dfs on components, do dgs on all unconnected, return total

        adj_list = [ [] for _ in range(n)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        # define dfs
        def dfs(node):
            if node in visited: 
                return 
            
            visited.add(node)
            for n in adj_list[node]:
                if n not in visited: 
                    dfs(n)


        count = 0
        # call dfs
        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1

        return count


