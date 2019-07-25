
class ListNode:
	
	def __init__(self,v):
		self.val = v
		self.next = None


class solution:

	def getLastNumberInLoop(self,n,m):
		head = ListNode(0)
		cur = head
		for i in range(1,n):
			node = ListNode(i)
			cur.next = node
			cur = node
		cur.next = head
		
		c = m-2
		p1,p2 = head,head.next
		while p2 and p2.next:
			if c:
				p1 = p1.next
				p2 = p2.next
				c-=1
			else:
				p1.next = p2.next
				p2 = p2.next
				p1 = p1.next
				p2 = p2.next
				c = m-2
		return p1.val
		
		
		
		
s = solution()
print(s.getLastNumberInLoop(5,2))