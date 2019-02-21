# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = None
        c = 0
        l3 = None
        start = None
        
        
        # if the first list is empty return the second list
        if(l1 == None):
            l = []
            start = l2
            while(start != None):
                l.append(start.val)
                start = start.next
            return l
        
        # if the second list is empty return the first list
        if(l2 == None):
            l = []
            start = l1
            while(start != None):
                l.append(start.val)
                start = start.next
            return l

        
        # While we reach end of any of the two lists we compare and place the smaller
        # element in the list l
        
        while(l1 != None and l2 != None):
            
            if(l1.val <= l2.val):
                l3 = ListNode(l1.val)
                
                l1 = l1.next
                
                if(c==0):
                    temp = l3
                    start = l3
                else:
                    temp.next = l3
                    temp = l3
                   
                
            else:
                
                l3 = ListNode(l2.val)
                
                l2 = l2.next
                if(c==0):
                    temp = l3
                    start = l3
                else:
                    temp.next = l3
                    temp = l3
            
            c = c + 1
            
        
        
        #if end of l1 is not reached add remaining elements of l1 list in linked list l3
       
        while(l1 != None):
            l3 = ListNode(l1.val)
            l1 = l1.next
            temp.next = l3
            temp = l3
        
        #if end of l2 is not reached add remaining elements of l2 list in linked list l3
        while(l2 != None and temp!=None):
            
            l3 = ListNode(l2.val)
            l2 = l2.next
            temp.next = l3
            temp = l3
        
        
        # Traverse the linkedlist l3 and convert it to a ordered list l
        l = []
        while(start != None):
            l.append(start.val)
            start = start.next
        
        
        return l