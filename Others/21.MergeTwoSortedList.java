/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
 
 /*
 * Purpose: Merge two sorted linked lists and return it as a sorted list. 
 * The list should be made by splicing together the nodes of the first two lists.
 */
 
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = null;
        ListNode tail = null;
        
        if( l1 == null ) return l2;
        if( l2 == null ) return l1;
        
        while( l1 != null && l2 != null ) {
            if( l1.val <= l2.val ) {
                if( tail == null ) {
                    tail = new ListNode(l1.val);
                    result = tail;
                }
                else{
                    tail.next = new ListNode(l1.val); 
                    tail = tail.next;
                }
                l1 = l1.next;
                
            } else {
                if( tail == null ) {
                    tail = new ListNode(l2.val);
                    result = tail;
                } else {
                    tail.next = new ListNode(l2.val); 
                    tail = tail.next;
                }
                
                 l2 = l2.next;
            }
            
        }
        
        if( l1 != null ) tail.next = l1;
        if( l2 != null ) tail.next = l2;
        
        return result;
    }
}
/*
* Runtime: 0 ms, faster than 100.00% of Java online submissions for Merge Two Sorted Lists.
* Memory Usage: 38.1 MB, less than 92.70% of Java online submissions for Merge Two Sorted Lists.
*/