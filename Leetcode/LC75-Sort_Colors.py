"""

two pointer 思路，把0放在左边，2放在右边，1跳过
zero，two 初始化分别是0,len(nums)-1 
分别表示0 和2 当前应该放的位置
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums)-1
        index = 0
        while index<=two:
            #  只有当前元素在zero指针前的时候才交换
            if nums[index] == 0 and index>zero:
                nums[index], nums[zero] = nums[zero], nums[index]
                zero += 1
            elif nums[index] == 2:
                nums[index], nums[two] = nums[two], nums[index]
                two-=1
            else:
                index+=1
        