class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adj list
        adj_list = [[] for n in range(numCourses)]        
        
        for u,v in prerequisites:
            adj_list[u].append(v)
        # list done

        # dfs this list:
        # visited set: 
        visited = set()
        curr_stack = set()
        result = []

        def dfs(node):
            # start from node, check if it is visited or in rec stack 
            # continuer with its corresponding neighbords dfs
            #once that is done, remoe this from wht recStck?
            if node in visited:
                return True
            if node in curr_stack:
                return False

         
            curr_stack.add(node)

            for n in adj_list[node]:
                if not dfs(n):
                    return False
            curr_stack.remove(node)
            visited.add(node)
            result.append(node)

            return True
        
        for node in range(numCourses):
            if not dfs(node):
                    return [] 
          
                
        return result







        