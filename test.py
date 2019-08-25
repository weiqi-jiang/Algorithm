import sys
lines = sys.stdin.readlines()
n,m = [int(num) for num in lines[0].strip().split(' ')]
ability = [max(int(a),0) for a in lines[-1].strip().split(' ')]
workload_pay = []
for line in lines[1:-1]:
    temp = [int(number) for number in line.strip().split(' ')]
    if temp:
        workload_pay.append(temp)

workload_pay.sort(key = lambda x: x[0])
for i in range(len(workload_pay)):
    if i>=1 and workload_pay[i][1]<=workload_pay[i-1][1]:
        workload_pay[i][1] = workload_pay[i-1][1]

        
for a in ability:
    print(binarySelection(a,workload_pay))
        
        
def binarySelection(skill,workload_pay):
    if skill <=0 or skill < workload_pay[0]:
        return 0
    left,right = 0,len(workload_pay)-1
    while left<=right:
        mid = (left+right)//2
        if mid<len(workload_pay)-1 and workload_pay[mid]<=skill and workload_pay[mid+1]>=skill:
            return workload_pay[mid][1]
        if workload[mid]>skill:
            right = mid -1 
        if workload[mid]<skill:
            left = mid + 1