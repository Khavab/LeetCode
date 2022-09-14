class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        temp, s = self, []
        while temp != None: 
            s += [temp.val]
            temp = temp.next
        return str(s)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1, t2, new, carry, current = l1, l2, ListNode(), 0, None
        while t1 != None or t2 != None:
            if current == None: current = new
            else: 
                current.next = ListNode()
                current = current.next
            
            num, carry = carry, 0
            if t1 != None: 
                num += t1.val
                t1 = t1.next
            if t2 != None: 
                num += t2.val
                t2 = t2.next
                
            if num > 9: carry, num = 1, num - 10
            
            current.val = num
            
            
        return new
    
l1 = ListNode(9)
temp = l1
for n in [9,9,9,9,9,9]:
    temp.next = ListNode(9)
    temp = temp.next
    
l2 = ListNode(9)
temp = l2
for n in [9,9,9]:
    temp.next = ListNode(9)
    temp = temp.next
print(l1)
print(l2)
print(Solution().addTwoNumbers(l1, l2))