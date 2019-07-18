class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        marjority,count = None,0
        for i in range(len(nums)):
            if count == 0:
                count +=1
                marjority = nums[i]
            elif nums[i]!= marjority:
                count -=1
            else:
                count +=1
        return marjority