"""
思路一： 第二次做这个题想出的思路，遍历，记录当前遇到的0的个数即为n
如果遇到非零值，设当前索引为m，则把当前值赋给m-n索引，设最后零值总数为N，遍历完之后
将数组末尾的N个元素全部赋值为0
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        if len(nums)<=1:
            return nums
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i-zeros] = nums[i]
        if zeros:
            nums[-zeros:] = [0]*zeros
                
"""
思路二： 这个思路有点讨巧，不太确定是否符合题意，遇到0就pop出来，然后末尾append一个0
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        n = len(nums)
        while p<n:
            if nums[p]==0:
                nums.pop(p)
                nums.append(0)
                n-=1
            else:
                p+=1
                 