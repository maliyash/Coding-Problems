/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
    public class Solution 
{
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) 
    {
        
     //calculating the length of A and B
        
        
     int countA = Solution.getLength(headA); 
     int countB = Solution.getLength(headB);
      
        
     //Calculating absolute difference of length
        
        int diff = java.lang.Math.abs(countA - countB);
     
        
     // Jump a nodes in longest Linked List   
        
        ListNode lon;
        ListNode small;
        if(countA>countB)
        {
            lon = Solution.jump(headA,diff);
            small= headB;
        }
        else
        {
            lon = Solution.jump(headB,diff);
            small= headA;
            
        }
     
        
        // Iterate until you reach the intersection
       
        while(lon!= small && lon!=null && small!=null)
        {
            lon = lon.next;
            small = small.next;
            
        }
        
        return lon;
            
    }
    
    
    public static int getLength(ListNode temp)
    {
        int i = 0;
        while(temp!=null)
        {
            i++;
            temp = temp.next;
        }
        
        return i;
    }
    
        
        public static ListNode jump(ListNode l, int diff)
        {
            
            while(diff!=0)
            {
                l = l.next;
                diff--;
                
            }
            
            return l;
        }
        
    
}