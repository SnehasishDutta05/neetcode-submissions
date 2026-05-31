# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        flag = 0 
        while(fast != None):
            slow = slow.next
            try: 
                fast = fast.next.next 
            except :
                return False
            if(fast == slow):
                return True
                break
        
        return False
        
        