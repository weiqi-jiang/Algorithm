#importation
import pandas as pd
import numpy as np
import utils


#data input
def read_input(inputPath):
	data = pd.read_csv(inputPath,header=None)
	for i in range(len(data)):
		data.iloc[i][0] = data.iloc[i][0].split(',')
	return data


#calc support score
def filterSupport(targets,countMap,total):
	#targets [[]] 形式
	collections = []
	blocks = []
	for target in targets:
		if calcSupport(target,countMap,total)>=utils.support_threshold:
			collections.append(target)
		else:
			blocks.append(target)
	return collections,blocks
			
def calcSupport(target,countMap,total):
	t = countMap[target[0]]
	for item in target:
		t = [i for i in t if i in countMap[item]]
	return len(t)/total


#calc confidence score
def filterConfidence(freq_collections, countMap, total):	
	rules = []
	for items in freq_collections:
		for item in items:
			x = [i for i in items if i!= item]
			y = [item]
			x_support = calcSupport(x,countMap,total)
			y_support = calcSupport(y,countMap,total)
			rule_confidence = x_support/y_support
			if rule_confidence > utils.confidence_threshold:
				rules.append(str(x) + "=>" + str(y))
	return rules
	
	
# permutation and combination
def combination(collections):
	result = []
	for i in range(len(collections)-1):
		for j in range(i+1,len(collections)):
			collection = tuple(set(collections[i]+collections[j]))
			result.append(collection)
	return set(result)



#获得第一次的备选集
def getFirstCandiate(allSample,countMap,total):
	s = set()
	for i in range(len(allSample)):
		for item in allSample.iloc[i][0]:
			s.add(item)
	result = []
	for i in s:
		result.append([i])
	itemset, blocks = filterSupport(result,countMap,total)
	return itemset, blocks


#过滤掉包含非频繁项集的集合
def filtering(collections, blocks):
	# collections 为set(tuple())形式 blocks list[list[]]形式
	blocks_set = [set(it) for it in blocks]
	result = []
	for c in collections:
		tmp = set(c)
		flag = True
		for b in blocks_set:
			if tmp>b:
				flag = False
				break
		if flag:
			result.append(list(c))
	return result
				
	


#计算单元集合的出现index
def calcCountMap(allSample):
	countmap = {}
	for i in range(len(allSample)):
		itemset = allSample.iloc[i][0]
		for item in itemset:
			if item in countmap:
				countmap[item].append(i)
			else:
				countmap[item] = [i]
	return countmap
	
	

#main func
def main():
	allSample = read_input(utils.inputData)
	freq_collections = []
	total = len(allSample)
	countMap = calcCountMap(allSample)

	curSet, blocks = getFirstCandiate(allSample,countMap,total)	
	flag = True
	while flag:
		newset = combination(curSet) #返回新的组合集合 set(tuple())type 
		filteredSet = filtering(newset,blocks) #滤掉那些包含了非频繁项集的集合
		statisedSet, newblocks  = filterSupport(filteredSet,countMap,total) #返回满足要求的组合集合
		curSet, blocks = statisedSet, newblocks
		if len(curSet)==0:
			flag = False
		else:
			freq_collections.extend(curSet)
	print('freq collection: ',freq_collections)
	#完成频繁项集的生成,接着对频繁项集依照confidence进行阈值过滤
	rules = filterConfidence(freq_collections,countMap,total)
	print(rules)
	
	
	
if __name__ =="__main__":
	main()