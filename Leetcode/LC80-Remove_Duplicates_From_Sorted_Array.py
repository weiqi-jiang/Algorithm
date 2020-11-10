"""
有点巧妙的思路
因为要求是最多重复两次，而且是sorted array，那么可以参考runner和walker的思路
two pointer index差值为2，那么如果p2==p1的时候 说明元素出现次数超过了2次
删除p2的元素，注意使用while loop
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return len(nums)
        
        p1, p2 = 0, 2
        while p2<=len(nums)-1:
            if nums[p2] == nums[p1]:
                nums.pop(p2)
            else:
                p1+=1
                p2+=1
        return len(nums)