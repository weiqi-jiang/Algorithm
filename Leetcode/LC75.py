class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,blue = -1, len(nums)-1
        i = 0
        while i<=blue:
            if nums[i] == 2:
                nums[i],nums[blue] = nums[blue],nums[i]
                blue -= 1
            if nums[i] == 0:
                nums[red+1],nums[i] = nums[i],nums[red+1]
                red+=1
                if i == len(nums)-1:
                    break
                else:
                    i+=1
            if nums[i]==1:
                i += 1
                