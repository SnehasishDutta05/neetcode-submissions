# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head):
        prev = None
        curr = head
        next = None
        while(curr != None):
            next = curr.next
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            head = None
            return head 

        head_new = self.reverse_ll(head)
        curr = head_new
        prev = None
        next = None
        
        if n == 1 :
            head_new = curr.next
            

        else:
            for i in range(n-1):
                prev = curr
                curr = curr.next
                next = curr.next 
            prev.next = next
        
        head_final = self.reverse_ll(head_new)
        return head_final





        