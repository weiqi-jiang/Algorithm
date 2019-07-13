class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False    
        
    
        for i in range(len(matrix)):
            if not matrix[i]:
                return False
            if matrix[i][0]>target:
                if i ==0:
                    return False
                else:
                    return self.binarySearch(matrix[i-1],0,len(matrix[i-1])-1,target)
            elif matrix[i][0]==target:
                return True
        return  self.binarySearch(matrix[-1],0,len(matrix[i-1])-1,target)
    
        
    def binarySearch(self,List, left,right,target):
        while left<=right:
            mid = (left+right)//2
            if List[mid] == target:
                return True
            elif List[mid]>target:
                right = mid -1
            else:
                left = mid + 1
        return False