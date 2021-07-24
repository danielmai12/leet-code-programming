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
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode listSum = null;
        ListNode tail = null; 
        int carry = 0;
        
        while( l1 != null || l2 != null ){
            int c = 0;
            
            if( l1 != null ){
                c += l1.val;
                l1 = l1.next;
            }
            
            if( l2 != null ){
                c += l2.val;
                l2 = l2.next;
            }
            
            c += carry;
            int newdigit = c % 10;
            
            carry = (c > 9)? 1 : 0;
            
            ListNode node = new ListNode(newdigit);
            
            if( tail != null ){
                tail.next = node;
                tail = tail.next; 
            }else{
                tail = node;
                listSum = tail;
            }
        }

        if( carry > 0 ){
            ListNode node = new ListNode(1);
            tail.next = node;
            tail = tail.next;
        }
        
        return listSum;
    }
}

/**
 * Runtime: 1 ms, faster than 100.00% of Java online submissions for Add Two Numbers.
 * Memory Usage: 38.9 MB, less than 96.92% of Java online submissions for Add Two Numbers.
 */
