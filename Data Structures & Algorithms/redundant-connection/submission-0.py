class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
  
        n = len(edges)
        parent = [i for i in (range(n+1))]
        rank = [0]*(n+1)
        def find(p):
            if parent[p]!=p:
                return find(parent[p])
            return parent[p]
            
        def union( a, b):
            x = find(a)
            y = find(b)
            # update edges based on rank. 

            if x == y:
                return False
            if rank[x]>rank[y]:
                parent[y] = x

            elif rank[y] > rank[x]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x]+=1
            return True

        res = []
        for a, b in edges:
            if not union( a,b):
                return [a,b]
        
        return []

            