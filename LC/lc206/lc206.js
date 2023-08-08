/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  var res = new ListNode();
  while(head){
      let tmp = res.next;
      res.next = new ListNode(head.val);
      res.next.next = tmp;
      head = head.next;
  }
  return res.next;
};