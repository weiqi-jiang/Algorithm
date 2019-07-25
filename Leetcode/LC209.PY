class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        temp = sum(nums)
        if temp < s:
            return 0
        if temp == s:
            return len(nums)
        return self.traverse(s,nums)
        
        
    def traverse(self,s,nums):
        left, right = 0,0
        cur_sum = 0
        # 由于在之前进行过判断，这里不需要判断 right 是否out of index
        while cur_sum<s:
            cur_sum += nums[right]
            right += 1
        minLength = right-left
        
        if right == len(nums):
            while True:
                cur_sum -= nums[left]
                if cur_sum == s:
                    left+=1
                elif cur_sum<s:
                    break
                left+=1
            minLength = min(minLength,right-left)
            return minLength
        
        while right<len(nums):
            cur_sum+= nums[right]
            while True:
                cur_sum -= nums[left]
                if cur_sum == s:
                    left+=1
                    break
                elif cur_sum <s:
                    cur_sum += nums[left]
                    break
                left += 1
            minLength = min(minLength,right-left+1)
            right+=1
            
        
        return minLength