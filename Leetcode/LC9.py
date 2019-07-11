class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        res  = []
        while left < right:
            if height[left]<height[right]:
                res.append((right-left)*height[left])
                temp = left + 1
                while height[temp]<=height[left] and temp <right:
                    temp += 1
                left = temp
            else:
                res.append((right-left)*height[right])
                temp = right -1
                while height[temp]<=height[right] and temp>left:
                    temp -= 1
                right = temp
        return max(res)