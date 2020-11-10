class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums2 and nums1:
            i,j = 0,0
            l1 = nums1[:m]
            l2 = nums2[:n]
            index = 0
            while i<m and j<n:
                if l1[i]<l2[j]:
                    nums1[index] = l1[i]
                    index +=1
                    i+=1
                else:
                    nums1[index] = l2[j]
                    index +=1
                    j+=1
            if i==m:
                while j<n:
                    nums1[index] = l2[j]
                    index+=1
                    j+=1
            if j==n:
                while i<m:
                    nums1[index] = l1[i]
                    index+=1
                    i+=1