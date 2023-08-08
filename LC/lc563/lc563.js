/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findTilt = function(root) {
  var tSum = function(t){
      if (!t) return 0;
      else return t.val + tSum(t.left) + tSum(t.right);
  };
  var helper = function(t){
      if (!t) return;
      else {let s1 = tSum(t.left), s2 = tSum(t.right);
      t.val = (s1 > s2) ? s1-s2 : s2-s1;
      helper(t.left);
      helper(t.right);
      return;}
  }
  helper(root);
  return tSum(root);
};