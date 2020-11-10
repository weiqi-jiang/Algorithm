"""
Linear Running Time but O(N) space complexity
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nummap = {}
        for i in range(len(nums)):
            if nums[i] not in nummap:
                nummap[nums[i]] = 1
            else:
                nummap[nums[i]] += 1
        for k,v in nummap.items():
            if v ==1:
                return k
"""
TC: O(NlogN)
SC: O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        p1,p2 = 0,2
        while p2<=len(nums)-1:
            if nums[p1] != nums[p2]:
                return nums[p1]
            p1+=3
            p2+=3
        return nums[-1]
        
"""
bit level operation
用一个INT 来保存每一个bit上1的次数，最后统一对3取余
如果一个数出现3次，那么1的次数对3取余为0，否则为1，之后这个INT就是出现一次的那个值
"""
