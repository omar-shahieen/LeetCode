class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        NOT_VISITED = 0
        VISITING = 1 
        VISITED = 2


        visited = [NOT_VISITED] * numCourses
        adj = defaultdict(list)


        for a ,b in prerequisites:
            adj[a].append(b)


        def dfs(v):
            if visited[v] == VISITING : return False
            if visited[v] == VISITED : return True


            visited[v] =  VISITING

            for E in adj[v]:
                if not dfs(E):
                    return False

            visited[v] = VISITED

            return True

        for v in range(numCourses):
            if visited[v] == NOT_VISITED:
                if not dfs(v):
                    return False

        return True


