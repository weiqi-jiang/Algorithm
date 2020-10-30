
	
def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


    
    
"""
选择排序
思路：  找到元素最小值，和第一个元素交换，找到剩下元素的最小值和第二个元素交换，直到最后交换完了整个列表
TC： (N-1) + (N-2) + ... + 1 = N(n-1)/2 = O(N^2)  最好最坏平均都是O(N^2)
SC：O(1) 原地排序
稳定性：元素发生交换，会出现相对位置的变化 例如 3 5 3 2
适用性： 都不太高效
"""
def selectSort(nums):
    for i in range(len(nums)):
        Min_index = i 
        for j in range(i+1, len(nums)):
            if nums[j]< nums[Min_index]:
                Min_index = j 
        nums[i], nums[Min_index] = nums[Min_index], nums[i]
    return nums 
  

"""
插入排序
思路：和洗牌一样，从第二个元素开始，如果比上一个元素小，就交换，直到找到合适的位置，这样前两个元素就是sorted，然后
从第三个元素开始，如果比上一个元素小，就交换直到找到合适的位置，以此类推
TC: 第2个元素需要最多1次判断，第三个元素需要最多2次判断，第n个元素需要最多n-1次判断，worst case 就是完全倒序的。O(n^2)
最好O(N),最坏O(N^2),平均O(N^2)
SC: O(1) 原地排序 
稳定性：稳定排序
适用性： 小规模或者基本有序时高效
"""   
def insertSort(nums):
    if len(nums)<=1:
        return nums 
    for i in range(1, len(nums)):
        ref = nums[i]
        for j in range(i-1, -1, -1):
            if nums[j] > ref:
                nums[j+1], nums[j] = nums[j], ref
            else:
                break
    return nums 
    
    
"""
冒泡排序
思路：每次比较左右两个大小，大的放右边，小的放左边。一轮下来，最大的就在最右边，然后比较第二轮。
TC: 平均O(N^2) 最好O(N) earlystop且已经sorted， 最坏O(N^2)
SC: O(1) 原地排序
稳定性：稳定的
适用性： 都不太高效 
"""   
def bubbleSort(nums):
    if len(nums)<=1:
        return nums 
    for i in range(len(nums)):
        for j in range(1,len(nums)-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums
            
# 优化版本 early stop, 如果一遍下来没有发生交换，说明左边已经是sorted了，就early stop 
def bubbleSort_v2(nums):
    if len(nums)<=1:
        return nums 
    for i in range(len(nums)):
        flag = True 
        for j in range(1, len(nums)-i): 
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                flag = False 
        if flag:
            return nums 
    return nums


"""
希尔排序
思路：直接插入排序的优化版本，插排适用小数据基本有序的情况，希尔排序针对大数据和无序进行了改良
把整个序列分割成若干子序列，子序列满足小数据，直接插入排序TC优良，然后减少子序列个数，增大子序列内部元素数，
此时子序列已经基本有序， 直接插入排序的TC依然优良
TC: 很复杂 和增量序列有关， 最差的情况是O(N^2), 最好O(N), 平均O(N^1.3)
SC: O(1)
稳定性：非稳定性，直接插入排序是稳定的
适用性：通用
"""        
def shellSort(nums):
    if len(nums)<=1:
        return nums 
    
    step = len(nums)//2 
    while step >0:
        for i in range(step, len(nums)):
            ref = nums[i]
            j = i 
            while j>=step:
                if nums[j-step] > nums[j]:
                    nums[j-step], nums[j] = nums[j], nums[j-step]
                    j -= step
                else:
                    break
        step = step // 2 
    return nums 

                
"""
归并排序
思路：divide and conquer 的思想，分而治之。 把序列分割成两部分，两部分再各自分割成两部分，最后分割成单个元素，
return的时候merge
TC: 最好最坏平均都是O(nlogn), 递归logN次，每次都需要N次比较
SC: O(N) 非原地排序
稳定性：稳定
适用性：通用
"""             
def mergeSort(nums):
    def _merge(nums1, nums2):
        p1, p2 = 0, 0 
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        res.extend(nums1[p1:])
        res.extend(nums2[p2:])
        return res
        
    if len(nums)<=1:
        return nums 
    left = mergeSort(nums[:len(nums)//2])
    right = mergeSort(nums[len(nums)//2:])
    return _merge(left, right)
 
# iteratively merge sort
def mergeSort_v2(nums):
    def _merge(nums1, nums2):
        p1, p2 = 0,0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1 
            else:
                res.append(nums2[p2])
                p2 += 1
        res.extend(nums1[p1:])
        res.extend(nums2[p2:])
        return res 
    if len(nums)<=1:
        return nums
    groups = [[_] for _ in nums]
    while len(groups)>1:
        tmp = []
        p1, p2 = 0, 1 
        while p1 < len(groups) and p2 < len(groups):
            tmp.append(_merge(groups[p1], groups[p2]))
            p1 += 2 
            p2 += 2
        if p1 < len(groups):
            tmp.append(groups[p1])
        groups = tmp
    return groups[0]

"""
快速排序
思路：divide and conquer 的思想，分而治之。 把序列分割成两部分，两部分再各自分割成两部分，最后分割成单个元素，
return的时候merge
TC: O(nlogn), 递归logN次，每次都需要N次比较
SC: O(N) 非原地排序
稳定性：稳定
适用性：
"""        
def quickSort(nums, left, right):
    def _partition(nums, left, right):
        pivot = nums[left]
        i, j = left+1, right 
        while True:
            while i <= j and nums[i] <= pivot:
                i += 1 
            while i<= j and nums[j] >= pivot:
                j -= 1
            if i>=j:
                break 
            nums[i], nums[j] = nums[j], nums[i]
        nums[left] = nums[j]
        nums[j] = pivot
        return j 
   
    if left>=right:
        return nums 
    mid = _partition(nums, left, right)
    nums = quickSort(nums, left, mid-1)
    nums = quickSort(nums, mid+1, right)
    return nums

    
if __name__  ==  "__main__":
    nums = [5,2,6,4,1]
    print(mergeSort_v2(nums))