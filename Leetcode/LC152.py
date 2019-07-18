class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[-1]
        if not nums:
            return 
            
            
        largest = [nums[0]]
        smallest = [nums[0]]
        for i in range(1, len(nums)):
            n1, n2 = nums[i]*largest[-1],  nums[i]*smallest[-1]
            largest.append(max(n1,n2,nums[i]))
            smallest.append(min(n1,n2,nums[i]))

        return max(largest)