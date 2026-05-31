# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        if A ==  None:
            return B 
        if B == None:
            return A
        if(A.val <= B.val):
            head = A 
            curr = A
            i = curr.next
            j = B
        else:
            head = B
            curr = B
            i = A 
            j = curr.next

        while (i!= None and j!= None):
            if(j.val < i.val ):
                curr.next = j
                j = j.next
                curr = curr.next
            else:
                curr.next = i
                i = i.next
                curr = curr.next 
        if j != None: 
            curr.next = j 
        else:
            curr.next = i 
        return head
            
        
        

        
        