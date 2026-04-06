class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqsMap = {i: [] for i in range(numCourses)}
        for crs1, crs2 in prerequisites:
            prereqsMap[crs1].append(crs2) # creating adjacency list
        
        states = [0] * numCourses # 0 for unvisited, 1 for visiting, 2 for visited

        def dfs(crs):
            state = states[crs]
            if state == 1:
                return False
            if state == 2:
                return True
            states[crs] = 1

            for neighbour in prereqsMap[crs]:
                if not dfs(neighbour):
                    return False
            
            states[crs] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
