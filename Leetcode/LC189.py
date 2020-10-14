"""
思路一： 参考solution中的circle replacement， 只需要O（1）的space
我们一个一个来完成替换，首先替换第一个，把index=0的元素放到它正确的位置上之后，现在我们手上是被替换的那个元素
接着把这个元素替换到正确的问题，一共替换N次就完成了，只需要一个tmp变量来保存当前的元素
但是有个问题，如果数组长度为9，右移3位 1，2，3，4，5，6，7，8，9， 1->4 4->7 7->1 结果变成了loop，就需要在形成loop之后，从下一个元素开始新循环
"""
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1:
            step = k%len(nums)
            if step:
                start = 0
                index = 0
                temp = None
                count = len(nums)
                last = nums[start]
                while count!=0:
                    index += step
                    if index>=len(nums):
                        index -= len(nums)
                    temp = nums[index]
                    nums[index] = last
                    last = temp
                    count-=1
                    if index == start:
                        index += 1
                        start+=1
                        last = nums[index]