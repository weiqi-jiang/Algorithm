class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        
        return self.bucket(nums,k,t)
        
        
        
    def bucket(self, nums, k, t):
        buckets = {}
        
        for i in range(len(nums)):
            # 这个细节很重要，假设t = 2 我们需要把3,4,5放在一起,因为3-5的abs 最大为2，所有要除以t+1 而不是t，如果/t 那就是2,3一起             #了
            b = nums[i]//(t+1)
            if b in buckets:
                return True
            if b-1 in buckets and abs(buckets[b-1]-nums[i])<=t:
                return True
            if b+1 in buckets and abs(buckets[b+1]-nums[i])<=t:
                return True
            
            buckets[b] = nums[i]
            if i>=k:
                del buckets[nums[i-k]//(t+1)]
        return False