"""
binarysearch的思路
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        
        def binarysearch(x, left, right):
            if left<=right:
                mid = (left+right)//2
 
                if mid**2 == x:
                    return mid 
                elif mid**2 > x:
                    return binarysearch(x, left, mid-1)
                else:
                    return binarysearch(x, mid+1,right)
            else:
                return right
        return binarysearch(x, 0, x)