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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
  var res = [];
  var helper = function(t){
      if (!t) return;
      else {
          helper(t.left);
          res.push(t.val);
          helper(t.right);
          return;
      }
  }
  helper(root);
  return res;
};