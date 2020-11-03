"""
有几个edge  case
[0] 如果长度为1 一定是true
[0, 1]  需要判断如果 首元素为0 返回False
[3,2,1,0,4] 对应代码中的情况

remain_steps保存当前index能往前跳的最大步数，如果为0，且不是最后一个index
那么就跳不过去了。
当前能往前跳的最大值等于max(上一步最大值-1，当前能跳的最大步数)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True 
        if nums[0] == 0:
            return False
        
        remain_steps = [0]*len(nums)
        remain_steps[0] = nums[0]
        for i in range(1,len(nums)):
            remain_steps[i] = max(remain_steps[i-1]-1, nums[i])
            # 对应上面
            if remain_steps[i] <=0 and i!=len(nums)-1:
                return False
        return True