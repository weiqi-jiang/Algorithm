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