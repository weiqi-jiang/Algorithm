class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        return self.mergeTwoList(pHead1,pHead2)
        
        
    def mergeTwoList(self,head1,head2):
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val<head2.val:
            mergenode = head1
            mergenode.next =  self.mergeTwoList(head1.next,head2)
        else:
            mergenode = head2
            mergenode.next = self.mergeTwoList(head1,head2.next)
        
        return mergenode