class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        return self.helper(version1,version2)
        
        
    def helper(self,v1,v2):
        v1 = [int(n) for n in v1.split('.')]
        v2 = [int(n) for n in v2.split('.')]
        i,j = 0,0
        while i<len(v1) and j < len(v2):
            if v1[i] == v2[j]:
                i,j = i+1,j+1
            else:
                if v1[i]>v2[j]:
                    return 1
                else:
                    return -1
        if i <len(v1):
            if sum(v1[i:]) >0:
                return 1
            else:
                return 0
        else:
            if sum(v2[i:])>0:
                return -1
            else:
                return 0