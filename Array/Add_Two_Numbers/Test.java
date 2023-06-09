public class Test {

    public static void main(String[] args) {
        // ListNode l1 = new ListNode(2);
        // ListNode l2 = new ListNode(4);
        // ListNode l3 = new ListNode(3);
        // l1.next = l2;
        // l2.next = l3;
        // ListNode ll1 = new ListNode(5);
        // ListNode ll2 = new ListNode(6);
        // ListNode ll3 = new ListNode(4);
        // ll1.next = ll2;
        // ll2.next = ll3;
        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(9);
        ListNode l3 = new ListNode(9);
        ListNode l4 = new ListNode(9);
        ListNode l5 = new ListNode(9);
        ListNode l6 = new ListNode(9);
        ListNode l7 = new ListNode(9);
        l1.next = l2;
        l2.next = l3;
        l3.next = l4;
        l4.next = l5;
        l5.next = l6;
        l6.next = l7;
        ListNode ll1 = new ListNode(9);
        ListNode ll2 = new ListNode(9);
        ListNode ll3 = new ListNode(9);
        ListNode ll4 = new ListNode(9);
        ll1.next = ll2;
        ll2.next = ll3;
        ll3.next = ll4;
        Solution s = new Solution();
        // s.printList(l1);
        // s.printList(ll1);
        s.printList(s.addTwoNumbers(l1, ll1));
    }

}