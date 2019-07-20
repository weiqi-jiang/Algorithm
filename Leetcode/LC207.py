class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = [0 for i in range(numCourses)]
        
        #计算每个节点的入度
        for e in prerequisites:
            indegrees[e[1]] += 1
        # 初始化链接列表
        al  ={}
        for i in range(numCourses):
            al[i] = []
        for e in prerequisites:
            al[e[0]].append(e[1])
        
        # 入度为零的点
        s = [i for i in range(numCourses) if indegrees[i] == 0]
        
        return self.kanh(indegrees,s,al,numCourses)
        
    def kanh(self,indegrees,s,al,numCourses):
        res = [i for i in range(numCourses)]
        while s:
            cur = s.pop()
            # 每有一个入度为零的点就pop出一个节点，最后如果不剩节点了就说明没有环，但是不在意到底pop的什么节点
            res.pop()
            nexts = al[cur]
            for node in nexts:
                # 把邻接点的入度减一
                indegrees[node]-=1
                if indegrees[node] == 0:
                    s.append(node)
        return len(res) == 0