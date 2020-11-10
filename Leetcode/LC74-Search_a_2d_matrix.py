"""
先找到所在的行
行内binarysearch
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(nums, left, right, target):
            if left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    return bs(nums, left, mid-1, target)
                else:
                    return bs(nums, mid+1, right, target)
            else:
                return False
            
        if not matrix:
            return False
        if not matrix[0]:
            return False
        left, right = 0, len(matrix[0])-1
        
        for row in range(len(matrix)):
            if matrix[row][0] == target:
                return True
            if matrix[row][0] > target:
                if row == 0:
                    return False 
                else:
                    return bs(matrix[row-1], left, right, target)
        return bs(matrix[-1], left, right, target)
    