
	
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



def fastSort(nums):
	if len(nums)<=1:
		return nums
	less = [nums[i] for i in range(1,len(nums))if nums[i]<=nums[0]]
	more = [nums[i] for i in range(1,len(nums))if nums[i]>nums[0]]
	return fastSort(less) +[nums[0]] + fastSort(more)
	
def bubbleSort(nums):
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i]>nums[j]:
				nums[i],nums[j] = nums[j],num[i]
	return nums



def mergeSort(nums):
	if len(nums)<=1:
		return nums
	mid = len(nums)//2
	left = mergeSort(nums[:mid])
	right = mergeSort(nums[mid:])
	return merge(left,right)
	
	
def merge(list1,list2):
	i,j = 0,0
	result = []
	while i<len(list1) and j<len(list2):
		if list1[i]<list2[j]:
			result.append(list1[i])
			i+=1
		else:
			result.append(list2[j])
			j+=1
	result+=list1[i:]
	result+=list2[j:]
	return result


    
   
    
    
"""
选择排序
思路：  找到元素最小值，和第一个元素交换，找到剩下元素的最小值和第二个元素交换，直到最后交换完了整个列表
TC： (N-1) + (N-2) + ... + 1 = N(n-1)/2 = O(N^2)
SC：O(1) 原地排序
稳定性：元素发生交换，会出现相对位置的变化 例如 3 5 3 2
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
SC: O(1) 原地排序 
稳定性：稳定排序
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
TC: O(N^2)
SC: O(1) 原地排序
稳定性：稳定的 
"""   
def bubbleSort(nums):
    if len(nums)<=1:
        return nums 
    for i in range(len(nums)):
        for j in range(1,len(nums)-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
        print(nums)
    return nums
            
    
    
    
    
    
    
    
    
    
    
    
if __name__  ==  "__main__":
    nums = [5,2,6,4,1]
    print(bubbleSort(nums))