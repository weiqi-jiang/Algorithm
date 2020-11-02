"""
思路一： two pointer， 很直接的思路，注意最外部使用while循环，不能使用for循环，因为过程中nums的长度会变化

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while nums:
            if i<len(nums)-1:
                if nums[i] == nums[i+1]:
                    nums.pop(i)
                else:
                    i+=1
            else:
                break
        return len(nums)
		
"""
思路二： LC beat 99%的思路，把所有不重复的元素提到数组最前面，然后删除掉后续元素

"""
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while (j < len(nums)):
            if (nums[i] == nums[j]):
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        del nums[i+1:]

        return(len(nums))