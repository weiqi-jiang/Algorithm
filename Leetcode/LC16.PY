class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 
        nums.sort()
        res = []

        for base in range(len(nums)-2):
            left,right = base+1,len(nums)-1
            while left < right:
                add = nums[left]+nums[right]+nums[base]
                res.append(add)
                if add == target:
                    # if the addition result equals exactly the target, no need to do extra calc
                    return target
                elif add > target:
                    right -=1 
                else:
                    left += 1
        
        tmp = [abs(a-target) for a in res]
        index = tmp.index(min(tmp))
        return res[index]