def insertSort(nums):
	leng = len(nums)
	for i in range(1,leng):
		key = nums[i]
		for j in range(i-1,-1,-1):
			if nums[j]>key:
				nums[j+1]=nums[j]
				nums[j]= key
			else:
				break
	return nums
	
	
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


#遍历， 每次找到最小的那个
def selectSort(nums):
	for i in range(0,len(nums)):
		Min = i
		for j in range(i+1,len(nums)):
			if nums[j]<nums[Min]:
				Min = j
		nums[i],nums[Min] = nums[Min], nums[i]
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

def main():
	nums = [5,2,8,7,5,10,9,4,1]
	print(insertSort(nums))
	print(bubbleSort(nums))
	print(fastSort(nums))
	print(selectSort(nums))
	print(mergeSort(nums))
	
if __name__  ==  "__main__":
	main()