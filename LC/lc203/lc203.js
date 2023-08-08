/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
  var res = new ListNode(0, head);
  var out = res;
  while(res.next){
      if (res.next.val == val){
          res.next = res.next.next;
      }
      else {res = res.next;}
  }
  return out.next;
};