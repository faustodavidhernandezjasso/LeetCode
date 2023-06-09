class Solution {


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode node = result;
        ListNode node1 = l1;
        ListNode node2 = l2;
        int carry = 0;
        int total;
        while (node1 != null && node2 != null) {
            total = carry + node1.val + node2.val;
            if (total > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            node.val = total % 10;
            node1 = node1.next;
            node2 = node2.next;
            if (node1 == null && node2 == null) {
                continue;
            }
            ListNode newNode = new ListNode();
            node.next = newNode;
            node = node.next;
        }
        while (node1 != null) {
            total = carry + node1.val;
            if (total > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            node.val = total % 10;
            node1 = node1.next;
            if (node1 == null) {
                continue;
            }
            ListNode newNode = new ListNode();
            node.next = newNode;
            node = node.next;
        }
        while (node2 != null) {
            total = carry + node2.val;
            if (total > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            node.val = total % 10;
            node2 = node2.next;
            if (node2 == null) {
                continue;
            }
            ListNode newNode = new ListNode();
            node.next = newNode;
            node = node.next;
        }
        if (carry != 0) {
            ListNode newNode = new ListNode(carry);
            node.next = newNode;
        }
        return result;
    }

    public ListNode generateList(int n) {
        int c = 0;
        ListNode list = new ListNode(c + 1);
        c += 1;
        ListNode node = list;
        while (c < n) {
            ListNode newNode = new ListNode(c + 1);
            node.next = newNode;
            node = node.next;
            c += 1;
        }
        return list;
    }


    /**
     * Imprimimos la lista.
     * @param l
     */
    public void printList(ListNode l) {
        ListNode node = l;
        while (node != null) {
            System.out.println(node.val);
            node = node.next;
        }
    }
}