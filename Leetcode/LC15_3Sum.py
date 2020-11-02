"""
在two sum的基础上，再加上一个维度罢了，固定一个数字的two sum
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            tmp = self.twoSum(nums,i+1,len(nums)-1,target)
            if tmp: 
                for t in tmp:
                    res.append([nums[i]]+t)
        return res 
    
    def twoSum(self,L,left,right,target):
        res  = []
        if len(L)<2:
            return res
        
        while left<right:
            if L[left] + L[right] == target:
                res.append([L[left],L[right]])
                left,right = left+1,right-1
                while left<right and L[left] == L[left-1]:
                    left += 1 
                while left < right and L[right] == L[right+1]:
                    right -= 1
            elif  L[left]+ L[right] > target:
                right -= 1
            elif  L[left]+ L[right] < target:
                left += 1
        return res