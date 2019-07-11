class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >0:
            if nums[i]>nums[i-1]:
                j = len(nums)-1
                while j>=i:
                    if nums[j]>nums[i-1]:
                        nums[j],nums[i-1] = nums[i-1],nums[j]
                        break
                    j-=1
                nums[i:] = sorted(nums[i:])
                break
                
            i -= 1
        if i==0:
            nums.sort()