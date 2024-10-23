
"""
Solution 1: One Loop
Complexity :
    Time Complexity: O(N)(1 Loop)
    Space Complexity: O(N) (length (l1 if len(l1) > len(l2) else l2)) 
"""
class ListNode:     
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        z = 0 
        while (l1 is not None or l2 is not None or z != 0):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            digit = (x+y+z)%10
            z = (x+y+z)//10
            newNode = ListNode(digit)
            head.next = newNode
            head = head.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return result.next