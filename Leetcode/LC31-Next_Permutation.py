"""
一个排列 最右边的元素如果是递减的，说明这部分元素已经是"最大的"，没有next permutation了
steps:
1. 首先 从右往左（递增） 找到第一个不是递增的元素，index = i 
2. 从右往左找到第一个大于index=i的元素，index=j
3. 交换i,j 
4. 
"""
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
            