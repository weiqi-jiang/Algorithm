"""
思路
1. 先按照首元素排序
2. 如果后一个list的首元素小于等于上一个list的末尾元素，就合并两个list
3. 合并后的list尾元素是两者较大值  [1,5],[2,3]这种情况就应该尾元素取5而不是3
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res  =[]
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if intervals[i][0]<=res[-1][1]:
                    res[-1][1] = max(res[-1][1],intervals[i][1])
                else:
                    res.append(intervals[i])
        return res