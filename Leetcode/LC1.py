class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        for i in range(len(nums)):
            if nums[i] in tempMap:
                tempMap[nums[i]].append(i)
                return tempMap[nums[i]]
            else:
                tempMap[target - nums[i]] = [i]