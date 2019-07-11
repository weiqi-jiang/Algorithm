class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        self.backtracking(n,n,"", 0,res)
        return list(set(res))
        
        
    def backtracking(self, left_num, right_num, cur, cur_count, res):
        '''
        left_num:剩下的可以用的左括号
        right_num:剩下的可以用的右括号
		cur 当前的组合
		cur_count 当前的count值，  "(" : -1     /   ")": +1 只有count值小于的时候才进行操作避免出现回括号太多的情况
		res 保存最后结果
		
        '''
        if not left_num and not right_num and not cur_count:
            res.append(cur)
            return
			
        if cur_count == 0 and left_num:
            self.backtracking(left_num-1,right_num,  cur+'(',cur_count-1,res)
        if cur_count <0:
            if left_num:
                self.backtracking(left_num-1,right_num,  cur+'(',cur_count-1,res)
            else:
                if right_num:
                    self.backtracking(0,0,cur+")"*right_num,0,res)
            if right_num:
                    self.backtracking(left_num,right_num-1,  cur+')',cur_count+1,res)