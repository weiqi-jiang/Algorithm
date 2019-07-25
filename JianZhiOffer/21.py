# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.curmin = None
        self.stack = []
        
    def push(self, node):
        # write code here
        if not self.curmin:
            self.curmin = node
        else:
            if node<self.curmin:
                self.curmin = node
        self.stack.append((node,self.curmin))
                
    def pop(self):
        # write code here
        if not self.stack:
            return None
        return self.stack.pop()[0]
    def top(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1][0]
    
    
    def min(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1][1]