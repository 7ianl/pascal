/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  a = new ListNode();
  let cur = a, c = 0;
  while (l1 || l2) {
      let sum = c + (l1 ? l1.val : 0) +
          (l2 ? l2.val : 0);
      cur.next = new ListNode(sum % 10);
      c = (sum >= 10) ? 1 : 0;
      cur = cur.next;
      if (l1) l1 = l1.next;
      if (l2) l2 = l2.next;
  }
  if (c) {cur.next = new ListNode(c)};
  return a.next;
};