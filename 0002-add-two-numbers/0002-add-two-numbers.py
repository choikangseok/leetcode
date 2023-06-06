# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # carry =[0]
        AnswerNode = head = ListNode(0)
        
        
        while True:
            temp = head.val
            head.next = ListNode((l1.val + l2.val+ temp)//10)
            head.val = (l1.val + l2.val+ head.val) % 10
            
            
            
            if l1.next ==None and l2.next ==None :
                if head.next.val == 0:
                    head.next=None
                break
            elif l1.next == None and l2.next != None :
                l1.next=ListNode(0)
            elif l1.next != None and l2.next == None :
                l2.next=ListNode(0)
                
            l1=l1.next
            l2=l2.next
            head= head.next
            
        
        return AnswerNode
        
        
        
        
        
        
        