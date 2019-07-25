class Solution:    
	def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        
        return self.helper(rotateArray)
        
    def helper(self,rotateArray):
        left,right = 0,len(rotateArray)-1
        while True:
            mid = (left+right)//2
            if right - left == 1:
                return rotateArray[right]
            if rotateArray[mid]>=rotateArray[left]:
                left = mid
            elif rotateArray[mid]<=rotateArray[right]:
                right = mid