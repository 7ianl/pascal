/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
  let ans = new ListNode(), cur = head, res = ans;
  for (i = 1; i < left; i++){
      res.next = new ListNode(cur.val);
      res = res.next;
      cur = cur.next;
  }
  for (i = left; i <= right; i++){
      let tmp = res.next;
      res.next = new ListNode(cur.val);
      res.next.next = tmp;
      cur = cur.next;
  }
  for (i = left; i <= right; i++){
      res = res.next;
  }
  while(cur){
      res.next = new ListNode(cur.val);
      res = res.next;
      cur = cur.next;
  }
  return ans.next;
};