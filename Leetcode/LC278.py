# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

"""
思路1： left可以等于right 这样就有可能不收敛，需要额外判断是否相等
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(left, right):
            if left<=right:
                mid = (left+right)//2
                if isBadVersion(mid):
                    if left == right:
                        return left
                    return helper(left, mid)
                else:
                    return helper(mid+1,right)
            return -1
        return helper(1,n)
        
        
        
"""
思路2： 在判断的时候 left 不能等于right
这样最后的时候收敛有两种可能，收敛在最后一个没问题的verison， 也可能收敛在最开始bad的version上，所以要再判断一遍
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = self.binarycheck(0,n)
        target = isBadVersion(index)
        if not target:
            return index+1
        else:
            return index
        
        
    def binarycheck(self,left,right):
        while left<right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
        return left