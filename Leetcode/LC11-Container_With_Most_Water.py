"""
从两边向中间逼近，每次短的一边向另一边移动，记录过程中的volume，其中的最大值就是全局最优。
也就是说每一种宽度其实就判断了一次。
这个题关键点在与想通为什么宽度为为width的容器最大值就是当前这一种情况
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max_volume = -1
        width = len(height)-1
        p1, p2 = 0, len(height)-1
        while p1<p2:
            if height[p1] < height[p2]:
                cur_volume = width * height[p1]
                max_volume = max(cur_volume, max_volume)
                p1+=1
                width-=1
            else:
                cur_volume = width * height[p2]
                max_volume = max(cur_volume, max_volume)
                p2-=1
                width-=1
        return max_volume


"""
优化版本，如果矮的一方向另一方移动的过程中遇到更矮的话，就没必要再判断容积，
接着往另一方向走
"""
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