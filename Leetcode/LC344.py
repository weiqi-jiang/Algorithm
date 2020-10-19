"""
思路一： two pointer
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        

"""
思路二： 递归， 和two pointer 方法其实是一样的，只是把two pointer的每次比较抽象成一个函数，然后递归调用而已
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, left, right):
            if left < right:
                s[left],s[right] = s[right], s[left]
                helper(s,left+1, right-1)
            else:
                return s 
        helper(s,0,len(s)-1)

"""
思路三： 较为复杂的一个递归，为了完成反转，可以先把左右反转，然后在左边列表的内部左右反转，右边列表的内部左右反转
递归，但是这种方式不方便replace in place, 而且麻烦
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s):
            if len(s)<=1:
                return s
            if len(s) == 2:
                return [s[1], s[0]]
            
            mid, left, right = [],[],[]
            if len(s)%2 == 1:
                mid = [s[len(s)//2]]
                left = s[:len(s)//2]
                right = s[len(s)//2+1:]
            else:
                mid = []
                left = s[:len(s)//2+1]
                right = s[len(s)//2+1:]
            return helper(right)+ mid +helper(left)
        print(helper(s))
        s = helper(s)