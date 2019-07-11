class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                t = target - nums[i]-nums[j]
                tmp = self.Sum(nums,left,right,t)
                if tmp:
                    for t in tmp:
                        res.append([nums[i],nums[j]]+t)
        return res
        
    def Sum(self,nums,left,right,target):
        res = []
        while left<right:
            if nums[left]+ nums[right] == target:
                res.append([nums[left],nums[right]])
                left,right = left+1,right -1
                while left<right and nums[left]==nums[left-1]:
                    left +=1 
                while left <right and nums[right] == nums[right+1]:
                    right -=1
            elif nums[left] + nums[right] > target:
                right -=1 
            else:
                left +=1
        return res