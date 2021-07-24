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
* Given the head of a linked list, remove the nth node from the end of the list and return its head.
* Hint: Maintain two pointers and update one with a delay of n steps.
*/

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode result = new ListNode(0, head);
        
        ListNode del_pointer = result;
        ListNode end_pointer = result;
        
        
        // Moves the end_pointer to the (n+1)_th nodes so that the gap between del_pointer and end_pointer.
        // is n nodes apart
        for( int i = 0; i <= n ; i++ ){
            end_pointer = end_pointer.next;
        }
        
        // Moving the end_pointer to the end and maintain the gap between del_pointer and end_pointer.
        while( end_pointer != null ){
            end_pointer = end_pointer.next;
            del_pointer = del_pointer.next;
        }
        
        // Delete the node n_th from the tail. 
        del_pointer.next = del_pointer.next.next; 
        
        
        return result.next;
    }
}
/*
* Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Nth Node From End of List.
* Memory Usage: 37.2 MB, less than 28.91% of Java online submissions for Remove Nth Node From End of List.
*/