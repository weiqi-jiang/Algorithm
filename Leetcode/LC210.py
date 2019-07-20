class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0 for i in range(numCourses)]
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        for e in prerequisites:
            indegree[e[0]] += 1
            adj_list[e[1]].append(e[0])
        
        
        order = self.topology(indegree,adj_list)
        if len(order) == numCourses:
            return order
        else:
            return []
        
        
        
        
    def topology(self,indegree,adj_list):
        stack = []
        order = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            cur = stack.pop(0)
            order.append(cur)
            connection = adj_list[cur]
            for c in connection:
                indegree[c] -= 1
                if indegree[c] == 0:
                    stack.append(c)
        return order