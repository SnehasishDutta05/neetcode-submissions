# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self,head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev  # new head






    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        while(fast != None and fast.next != None):
            slow = slow.next 
            fast = fast.next.next 
        head1 = head 
        head2 = slow.next
        slow.next = None

        head2 =  self.reverseList(head2)

        while(head1 != None and head2 != None):
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1 
            head2 = temp2 
        
        


        