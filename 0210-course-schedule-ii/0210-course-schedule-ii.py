class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        if there is back edge return []
        apply topological sort
        """

        NOT_VISITED , VISITING , VISITED = 0 , 1 ,2 
        visited = [NOT_VISITED] * numCourses
        adj = defaultdict(list)

        for a, b in prerequisites :
            adj[b].append(a)


        res = []

        def dfs(v):
            if visited[v] == VISITING : return False
            if visited[v] == VISITED : return True

            visited[v] = VISITING

            for E in adj[v]:
                if not dfs(E):
                    return False


            res.append(v)
            visited[v] = VISITED

            return True
            



        for v in range(numCourses):
           if not dfs(v):
                return []

        return res[::-1]